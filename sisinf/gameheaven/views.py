from django.shortcuts import render, redirect
from django.http import HttpResponse
from gameheaven.models import Cliente, Tienda
from gameheaven.Constantes import ConstantesVOs as Constantes
from gameheaven.DAOs import daoUsuario
from gameheaven.DAOs import daoTienda
from django.contrib.auth import authenticate, login, logout
from gameheaven.forms import RegisterForm


from .forms import *


from gameheaven.templates import *

# Create your views here.

def default(request):
    return render(request, 'main/base.html')


def loginUser(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {"form": form})

    # ÁLVARO TU CÓDIGO ES EL DE ABAJO, EL DE ARRIBA ES PARA EL FORMULARIO NO BORRAR

    """
    if request.method != 'POST':
        return
    try:
        email = request.POST[Constantes.EMAIL]
        password = request.POST[Constantes.PASSWORD]
    except:
        
    if(daoUsuario.existeUsuario(email) != True):
        return HttpResponse("El usuario no existe")
    if(daoUsuario.checkPassword(email, password) != True):
        return HttpResponse("Contraseña incorrecta")

    return render(request, 'inicio.html') """


def createCliente(request):


    if request.method == 'POST':
        form = RegisterForm(request.POST)
        
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {"form": form})


    # ÁLVARO TU CÓDIGO ES EL DE ABAJO, EL DE ARRIBA ES PARA EL FORMULARIO NO BORRAR


    pass
    
    if request.method != 'POST':
        return
    try:
        email = request.POST[Constantes.EMAIL]
        usuario = request.POST[Constantes.USUARIO]
        password = request.POST[Constantes.PASSWORD]
        tienda = Tienda(ciudad="Madrid", codigoPostal = "22005")
        daoTienda.newTienda(tienda)
    except:
        return HttpResponse("Error al crear el cliente")
    
    if(daoUsuario.existeUsuario(email)):
        return HttpResponse("El email ya existe")
    
    cliente = Cliente(email=email, usuario=usuario, password=password, tienda=tienda)
    daoUsuario.newCliente(cliente)
    return render(request, 'inicio.html')

    