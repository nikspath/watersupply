from django.shortcuts import render,redirect


from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView


# Create your views here.\

def second(request):
	return render(request,'showmany.html',{'mes':"second"})

def first(request):
    return render(request,'showmany.html',{'mes':'nikhl'})

def third(request):
	return render(request,'showmany.html',{'mes':'thied'})
