from django.conf.urls import url,include
from django.contrib import admin
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^first',first),
   url(r'^second',second),
   url(r'^third',third),



]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)