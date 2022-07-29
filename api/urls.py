from django.urls import path
from . import views

urlpatterns=[
    path('blog/', views.BlogListCreate.as_view()),
    path('blog/<int:pk>', views.BlogRetriveUpdateDestroy.as_view()),
    path('signup-rqz/', views.signup),
    path('login/', views.login),
    path('newsletter/', views.NewsletterCreate.as_view()),
    path('sendmail/', views.send_email),
]
