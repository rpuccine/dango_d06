from django import forms

class LogInForm(forms.Form):
	name = forms.CharField(max_length=32)
	password = forms.CharField(max_length=32, widget=forms.PasswordInput)

class SignInForm(forms.Form):
	name = forms.CharField(max_length=32)
	password = forms.CharField(max_length=32, widget=forms.PasswordInput)
	cf_password = forms.CharField(max_length=32, widget=forms.PasswordInput)
