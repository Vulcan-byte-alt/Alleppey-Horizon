from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User #modifies User using this form 
        fields = ["username","email","password1","password2"] #specfies the order of fields for email to be displayed
