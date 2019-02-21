# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from property.models import mainproperty,followproperty
from django.http import JsonResponse
import json

# Create your views here.
def getfilterdataview(request):
	return JsonResponse({'obj':request.GET.get('priceslider')})

def searchproview(request):
	qr=mainproperty.objects.searchbyfilter(request.GET.get('q'))
	return render(request,'dashboard.html',{'list':qr})

def saveinerest(request):
	o=request.GET.get('q')
	mainobj=mainproperty.objects.get(id=o)
	sv=followproperty(user=request.session.get('usrname'),propertyid=mainobj)
	sv.save()
	cnt=followproperty.objects.all().count()
	request.session['propertycnt']=cnt
	return JsonResponse({'obj':cnt})

def godashboard(request):
	return redirect('/dashboard/')

def index(request):
	mp=mainproperty.objects.all()
	return render(request,'dashboard.html',{'list':mp})

def followpropertyview(request):
	fo=followproperty.objects.all()
	return render(request,'followproperty.html',{'follow':fo})



def searchproperty(request):
	search=request.GET.get('q')
	mainproperty.objects.searchproperty(search)	
