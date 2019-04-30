from django.conf.urls import url
from django.contrib import admin
from .views import *

urlpatterns = [
	url(r'^$',bookingformview.as_view(),name='addbooking'),
    url(r'^booking/', bookingformview.as_view(),name='addbooking'),
    url(r'^gettotalamount',gettotalamount),
    url(r'^bookingList',bookingList.as_view()),
    url(r'^getbookingdata',getbookingdata),
    url(r'^getDUEbookingdata',getDueBookingList),
    url(r'^FilterData',fullFilterData),
    url(r'^getCollection',getCollection),
    
]



