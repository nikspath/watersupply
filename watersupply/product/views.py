from django.shortcuts import render,redirect
from .forms import bookingForm
from django.http import JsonResponse
from .models import productlist,Booking
from django.views.generic import FormView,ListView
from django.core import serializers
import json

# Create your views here.


def getbookingdata(request):
	qr=Booking.objects.filterdatasearch(request.GET.get('date'))
	data=serializers.serialize('json',qr)
	return JsonResponse({'data':data})

def getbookinglist(request):
	qr=Booking.objects.fullFilterData(request)
	return qr


def fullFilterData(request):
	qr=Booking.objects.fullFilterData(request)
	data=serializers.serialize('json',qr)
	return JsonResponse({'data':data})


# class bookingsdetails(DetailView):
# 	template_name='product/booking_detail.html'
	
# 	def get_context_data(self,)

def getCollection(request):
	qr=Booking.objects.calculatedData()
	#dt=serializers.serialize('json',qr)
	return JsonResponse({'data':qr})

class bookingList(ListView):
	template_name='Booking_list.html'
	model=Booking

	def get_context_data(self,*args,**kwargs):
		context=super(bookingList,self).get_context_data(**kwargs)
		context['list']=Booking.objects.fullFilterData(self.request)
		context['totalcollection']=Booking.objects.calculatedData()
		return context



def getDueBookingList(request):
	qr=Booking.objects.getDueBookingList()
	dt=serializers.serialize('json',qr)
	return JsonResponse({'data':dt})

class bookingformview(FormView):
	form_class=bookingForm
	template_name='product/bookingform.html'

	def post(self,request,*args,**kwargs):
		form=self.form_class(request.POST)
		if form.is_valid():
			productB=request.POST.get('productB')
			quantityB=request.POST.get('quantityB')
			payAmtB=request.POST.get('payAmtB')
			customernameB=request.POST.get('customernameB')
			customerAddressB=request.POST.get('customerAddressB')
			totalprizeB=request.POST.get('totalprizeB')

			checkbx=False
			if totalprizeB == payAmtB:
				checkbx=True
			mobileB=request.POST.get('mobileB')
			
			sv=Booking(productB=productlist.objects.get(id=productB),payAmtB=payAmtB,mobileB=mobileB,isFullPayB=checkbx,
				quantityB=quantityB,customernameB=customernameB,customerAddressB=customerAddressB,
				totalprizeB=totalprizeB)
			sv.save()
			dt=getbookinglist(request)
			return render(request,self.template_name,{'form':form,'list':dt})	
		dt=getbookinglist(request)	
		return render(request,self.template_name,{'form':form,'list':dt})

	def get(self,request,*args,**kwargs):
		form=self.form_class()

		dt=getbookinglist(request)
		return render(request,self.template_name,{'form':form,'list':dt})




def gettotalamount(request):
	pid=request.GET.get('id')		
	qr=productlist.objects.filter(id=pid)
	data=serializers.serialize('json',qr)
	return JsonResponse({'data':data})
