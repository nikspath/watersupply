from django import forms


class custregform(forms.Form):
	custname=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
	custlast=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
	custemail=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
	custmobile=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
	custpassword=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
		

class custloginform(forms.Form):
	custusr=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
	custpass=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
