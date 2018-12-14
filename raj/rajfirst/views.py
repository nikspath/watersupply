from django.shortcuts import render,redirect
from .models import rajuserfirst
from .forms import rajuserfirstform
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView


# Create your views here.\


class RajList(ListView):
	model=rajuserfirst
	fields='__all__'
	template_name='rajuserfirst_list.html'

def second(request):
	return render(request,'showmany.html',{'mes':"second"})

def first(request):
	fm=rajuserfirstform(request.POST or None,request.FILES or None)
	if fm.is_valid():
		ru=request.POST['rajuser']
		rm=request.FILES['rajimg']
		sv=rajuserfirst(rajuser=ru,rajimg=rm)
		sv.save()
		return redirect('rajlist')
	return render(request,'rajfirst/rajshowfirst_form.html',{'form':fm})

def third(request):
	return render(request,'showmany.html',{'mes':'thied'})
