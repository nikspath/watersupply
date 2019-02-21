from django import forms


class mainpropertyform(forms.Form):
	propertyname=forms.CharField(max_length=200)
	propertydesc=forms.CharField(max_length=255)
	propertytype=forms.CharField(max_length=200)
	propertyrate=forms.CharField(max_length=200)
	propertyimg=forms.FileField(upload_to='media/images/')