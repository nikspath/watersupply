from django.db import models
from django.db.models import Q

# Create your models here.

class mainpropertyManager(models.Manager):
	def searchbyfilter(self,qry):
		lookup=(Q(propertyname__icontains=qry)|
				Q(propertydesc__icontains=qry) |
				Q(propertytype__icontains=qry))
		return self.get_queryset().filter(lookup)

class mainproperty(models.Model):
	propertyname=models.CharField(max_length=200)
	propertydesc=models.CharField(max_length=255)
	propertytype=models.CharField(max_length=200)
	propertyrate=models.CharField(max_length=200)
	propertyimg=models.FileField(upload_to='media/images/')


	def __str__(self):
		return self.propertyname

	objects=mainpropertyManager()	



class followproperty(models.Model):
	user=models.CharField(max_length=200)
	propertyid=models.ForeignKey('mainproperty',on_delete=models.CASCADE)
	timestamp=models.DateTimeField(auto_now_add=True)		