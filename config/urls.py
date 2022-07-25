from django.contrib import admin
from django.contrib.admin.options import settings
from django.urls import path, include, re_path
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    # re_path('.*',TemplateView.as_view(template_name='index.html')),

]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
