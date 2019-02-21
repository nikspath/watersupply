# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class custreg(models.Model):
	custname=models.CharField(max_length=200)
	custlast=models.CharField(max_length=200)
	custemail=models.CharField(max_length=255,unique=True)
	custmobile=models.CharField(max_length=15,unique=True)
	custpassword=models.CharField(max_length=200,unique=True)
	custtimestamp=models.DateTimeField(auto_now_add=True)	
