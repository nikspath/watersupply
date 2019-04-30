from django import forms
from .models import productlist

class bookingForm(forms.Form):
	CHOICE=[(i.id,i.nameP) for i in productlist.objects.all()]
	productB=forms.ChoiceField(choices=CHOICE,widget=forms.Select(attrs={'class':'form-control'}))
	quantityB=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
	customernameB=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	customerAddressB=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':'3'}))
	payAmtB=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
	totalprizeB=forms.CharField(widget=forms.HiddenInput(attrs={'id':'id_totalprizeB'}))
	mobileB=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	isFullPayB=forms.BooleanField(widget=forms.CheckboxInput(),required=False)