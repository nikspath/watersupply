from django.conf.urls import url
from django.contrib import admin
from .views import *


urlpatterns = [
    url(r'^saveinerestp',saveinerest),
    url(r'^dashboard',index,name='dashboard'),
    url(r'^followproperty',followpropertyview),
    url(r'^searchproperty',searchproview),
    url(r'^getfilterdata',getfilterdataview),
] 
