from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from gameheaven.DAOs import daoTienda


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(widget=forms.PasswordInput, label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    tienda = forms.ChoiceField(choices=[(x, x) for x in daoTienda.getAllTiendas()])
    
    class Meta:
        model = User
        fields = ["email", "password1", "password2"]


class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    
    class Meta:
        model = User
        fields = ["email", "password"]