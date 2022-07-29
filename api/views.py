
from email import message
from rest_framework import generics
from .serializers import BlogSerializer, NewsletterSerializer
from blog.models import Blog
from blog.permissions import IsAuthorOrReadOnly
from django.db import IntegrityError
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from rest_framework.parsers import MultiPartParser, FormParser
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings

# Create your views here.

class BlogListCreate(generics.ListCreateAPIView):
    serializer_class = BlogSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = (IsAuthorOrReadOnly,)

    def get_queryset(self): 
        return Blog.objects.all().order_by('-created')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BlogRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BlogSerializer
    permission_classes = (IsAuthorOrReadOnly,)

    def get_queryset(self):
        return Blog.objects.all()

class NewsletterCreate(generics.CreateAPIView):
    serializer_class = NewsletterSerializer


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            user = User.objects.create_user(
                username=data['username'],
                password=data['password'],
            )

            user.save()
            token = Token.objects.create(user=user)

            return JsonResponse({ 'token': str(token) }, status=201)
        except IntegrityError:
            return JsonResponse({ 'error': 'Username taken. Choose another.' }, status=400)


@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user = authenticate(
            request,
            username = data['username'],
            password = data['password'],
        )
        if user is None:
            return JsonResponse(
                { 'Error': 'Unable to login. Username and password are incorrect' },
                status=400
            )
        else:
            try: # Return a user token
                token = Token.objects.get(user=user)
            except:# If not exist, create a new one
                token = Token.objects.create(user=user)

            return JsonResponse(
                { 'token': str(token) },
                status=201
            )

            
@csrf_exempt
def send_email(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        name = data['name']
        email = data['email']
        company = data['company']
        message = data['message']
        try:
            send_mail(
                subject='Persona buscando contacto de gruporequiez.com',
                message=f'Nombre: {name} \n Correo: {email} \n Mensaje: {message} \n Compañía: {company}',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.RECIPIENT_ADDRESS],
                fail_silently=False,
            )
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponse('Mensaje enviado con exito')
    else:
        return HttpResponse('Error al enviar el mensaje!')