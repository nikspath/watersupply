from django.conf.urls import url
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^custregister/', custregview),
    url(r'^custlogin/',custloginview,name='custlogin'),
    url(r'^logout/',custlogout),
]
