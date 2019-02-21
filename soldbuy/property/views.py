from django.shortcuts import render
from .forms import *
from .models import *
# Create your views here.


def saveproperty(request):
	fm=mainpropertyform()
	return render(request,'propertyform.html',{'form':fm})

	