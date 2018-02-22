from django import forms
from .models import Game
from django.contrib.auth.models import User
from django.db import models

class GameForm(forms.ModelForm):
	class Meta:
		model = Game
		fields = '__all__'

class LoginForm(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput())

class UserRegisterForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'first_name', 'last_name', 'password']
		widgets = {
			"password": forms.PasswordInput()
		}