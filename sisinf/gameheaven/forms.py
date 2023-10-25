from django import forms
from django.contrib.auth.forms import UserCreationForm
from gameheaven.models import Usuario, Tienda
from gameheaven.DAOs import daoTienda,daoUsuario
from django.forms import ModelChoiceField
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    username = forms.CharField(required=True, label="Username")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    # Define a ModelChoiceField for the 'tienda' field
    tienda = ModelChoiceField(
        queryset=Tienda.objects.all(),  # Provide a queryset of Tienda instances
        empty_label=None,  # Optionally, you can set an empty_label to None if needed
        label="Tienda"
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        if password and password2 and password != password2:
            self.add_error("password", "Las contraseñas no coinciden")
            self.add_error("password2", "Las contraseñas no coinciden")

    def clean_username(self):
        username = self.cleaned_data["username"]
        if daoUsuario.existeUsuarioUsername(username):
            raise ValidationError("El nombre de usuario ya existe.")
        return username

    def clean_email(self):
        email = self.cleaned_data["email"]
        if daoUsuario.existeUsuarioEmail(email):
            raise ValidationError("El correo electrónico ya está registrado.")
        return email
    
    
    class Meta:
        model = Usuario
        fields = ["email", "username", "tienda", "password", "password2"]


class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, label="Password")

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        if not daoUsuario.existeUsuarioEmail(email):
            self.add_error("email", "El correo electrónico no está registrado.")
        elif not authenticate(email=email, password=password):
            self.add_error("password", "Contraseña incorrecta.")
    
    class Meta:
        model = Usuario
        fields = ["email", "password"]