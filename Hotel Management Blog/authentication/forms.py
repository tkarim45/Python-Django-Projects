from django import forms
from django.forms import ModelForm
from .models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
   username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
   first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
   last_name = forms.CharField(widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'})))
   email = forms.EmailField(widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'})))
   password1 = forms.CharField(widget=(forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})))
   password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))
   user_type = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'User Type', 'value': '' ,'id': 'userType', 'type': 'hidden'}))
    
   
   class Meta:
      model = User
      fields = ("username", "email", "first_name", "last_name", "user_type")

