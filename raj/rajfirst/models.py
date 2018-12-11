from django.db import models
from django.urls import reverse

# Create your models here.


class rajuserfirst(models.Model):
	rajuser=models.CharField(max_length=30,default=None)
	rajimg=models.FileField(upload_to='media/image/',default=None)

	def get_detail_url(self):
		return "/detail/{}".format(self.rajuser)	
		
	def get_absolute_url(self):
		return reverse('rajlist')	

	def __str__(self):
		return self.rajuser



class rajshowfirst(models.Model):
	rajshowuser=models.ManyToManyField('rajuserfirst')
	rajshowemail=models.CharField(max_length=30)	

	def get_absolute_url(self):
		return reverse('rajlist')	


