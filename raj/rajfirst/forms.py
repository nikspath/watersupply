from django import forms
from .models import rajuserfirst

class rajuserfirstform(forms.Form):
	rajuser=forms.CharField(widget=forms.TextInput())
	rajimg=forms.FileField(widget=forms.FileInput())



class rajshowfirstform(forms.Form):
	a=[(x.rajuser,x.rajuser) for x in rajuserfirst.objects.all()]
	rajshowuser=forms.ChoiceField(choices=a)
	rajshowemail=forms.CharField(widget=forms.TextInput())
