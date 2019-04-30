from django.db import models
from django.db.models import Q,Sum
from datetime import datetime
import operator
from functools import reduce
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your models here.


class productlist(models.Model):
	nameP=models.CharField(max_length=200)
	categoryP=models.CharField(max_length=200)
	priceP=models.DecimalField(max_digits=6,decimal_places=2)
	timestampP=models.DateTimeField(auto_now_add=True)
	imageP=models.FileField(upload_to='media/image/')

	def __str__(self):
		return self.nameP




class BookingManager(models.Manager):

	def filterdatasearch(self,qry):
		filterloop=Q(dateB=qry)
		dt=self.get_queryset().filter(filterloop)
		return dt

	def calculatedData(self):
		total_coln=self.get_queryset().aggregate(Sum('totalprizeB'),Sum('payAmtB'))
		due_col=total_coln['totalprizeB__sum']-total_coln['payAmtB__sum']
		dt={'tot_col':total_coln['totalprizeB__sum'],'tot_pay_col':total_coln['payAmtB__sum'],'due_col':due_col}
		return dt

	def getDueBookingList(self):
		qr=self.get_queryset().filter(isFullPayB=False)
		return qr

	def fullFilterData(self,request):
		lookup=[]
		if request.GET.get('datepick'):
			lookup.append(Q(dateB__range=([request.GET.get('datepick'),request.GET.get('datepick')])))
		if request.GET.get('searchtxt'):
			lookup.append(Q(customernameB__icontains=request.GET.get('searchtxt'))|Q(mobileB__iexact=request.GET.get('searchtxt')))
		if not lookup :
			qr=self.get_queryset().all().order_by('-id')
		else:
			qr=self.get_queryset().filter(reduce(operator.and_, lookup)).order_by('-id')		
		
		page=request.GET.get('page',1)
		data=self.createpagination(qr,page)
		return data

	def createpagination(self,qr,page):
		pg=Paginator(qr,5)
		try:
			dt=pg.page(page)
		except PageNotAnInterger:
			dt=pg.page(1)
		except EmptyPage:
			dt=pg.page(pg.num_pages)			
		return dt	



class Booking(models.Model):
	productB=models.ForeignKey(productlist)
	quantityB=models.IntegerField()
	customernameB=models.CharField(max_length=200)
	customerAddressB=models.TextField()
	payAmtB=models.DecimalField(max_digits=7,decimal_places=2,default=0.00)
	totalprizeB=models.DecimalField(max_digits=6,decimal_places=2)	
	mobileB=models.CharField(max_length=20,null=True,blank=True)
	isFullPayB=models.BooleanField(default=False)
	timestampB=models.DateTimeField(auto_now=True)
	dateB=models.DateField(default=datetime.today().strftime('%Y-%m-%d'),null=True,blank=True)


	objects=BookingManager()


