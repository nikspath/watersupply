# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import custregform,custloginform
from  .models import custreg
from property.models import followproperty 
# Create your views here.

def custlogout(request):
	del request.session['usrname']
	del request.session['custmob']
	del request.session['propertycnt']
	return redirect('dashboard')

def custloginview(request):
	fm=custloginform(request.POST)
	if fm.is_valid():
		custuser=request.POST.get('custusr')
		custpass=request.POST.get('custpass')
		res=custreg.objects.filter(custmobile=custuser,custpassword=custpass)
		if res.count() == 1:
			for i in res:
				cnt=followproperty.objects.all().count()
				request.session['propertycnt']=cnt
				request.session['usrname']=i.custname
				request.session['custmob']=custuser
			return redirect('dashboard')
	return render(request,'custlogin.html',{'form':fm})	


def custregview(request):
	fm=custregform(request.POST)
	if fm.is_valid():
		custname=request.POST.get('custname')
		custlast=request.POST.get('custlast')
		custemail=request.POST.get('custemail')
		custpassword=request.POST.get('custpassword')
		custmobile=request.POST.get('custmobile')
		sv=custreg(custname=custname,custlast=custlast,custemail=custemail,custpassword=custpassword,custmobile=custmobile)
		sv.save()
		return redirect('custlogin')

	return render(request,'custregister.html',{'form':fm}) 