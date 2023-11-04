from django import forms
from django.contrib.auth.forms import UserCreationForm
from gameheaven.models import Usuario, Tienda
from gameheaven.DAOs import daoTienda,daoUsuario
from django.forms import ModelChoiceField
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, password_validation



class RegisterForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(required=True, label="Username")
    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=("Password confirmation"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=("Enter the same password as before, for verification."),
    )
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

        try:
            password_validation.validate_password(password, self.instance)
        except ValidationError as error:
            self.add_error("password", error)

        if cleaned_data.get("username") in password:
            self.add_error("password", "La contraseña no puede ser similar al nombre de usuario")
        if password != password2:
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

class SendEmailForm(forms.Form):
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        subject = cleaned_data.get("subject")
        message = cleaned_data.get("message")

        if email == "" or email == None or subject == "" or subject == None or message == "" or message == None:
            self.add_error("email", "Ningún campo puede estar vacío.")
        
    
    class Meta:
        model = Usuario
        fields = ["email", "subject", "message"]

class AddProductForm(forms.Form):
    nombre = forms.CharField(required=True)
    descripcion = forms.CharField(required=True)
    valoracion = forms.FloatField(required=True)
    plataformas = forms.CharField(required=False)
    img = forms.ImageField(required=False)
    precio = forms.FloatField(required=True)

class AddStockForm(forms.Form):
    stock = forms.IntegerField(required=True)


class ChangeShopForm(forms.Form):
    tienda = forms.ModelChoiceField(queryset=Tienda.objects.all(), empty_label=None, label="Tienda")

class AddWorkerAccount(forms.ModelForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(required=True, label="Username")
    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=("Password confirmation"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=("Enter the same password as before, for verification."),
    )
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

        try:
            password_validation.validate_password(password, self.instance)
        except ValidationError as error:
            self.add_error("password", error)

        if cleaned_data.get("username") in password:
            self.add_error("password", "La contraseña no puede ser similar al nombre de usuario")
        if password != password2:
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

class AddShopForm(forms.Form):
    ciudad = forms.CharField(required=True, label="Ciudad")
    codigoPostal = forms.CharField(required=True, label="Código Postal")

    def clean(self):
        cleaned_data = super().clean()
        ciudad = cleaned_data.get("ciudad")
        codigoPostal = cleaned_data.get("codigoPostal")

        if daoTienda.existeTienda(ciudad, codigoPostal):
            self.add_error("ciudad", "Ya existe una tienda en esa ciudad con ese código postal.")

    class Meta:
        model = Tienda
        fields = ["ciudad", "codigoPostal"]