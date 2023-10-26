from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from gameheaven.models import Cliente, Tienda, Usuario
from gameheaven.Constantes import ConstantesVOs as Constantes
from gameheaven.DAOs import daoUsuario
from gameheaven.DAOs import daoTienda
from django.contrib.auth import authenticate, login, logout
from gameheaven.forms import RegisterForm, LoginForm
from django.contrib.auth import logout


from .forms import *


from gameheaven.templates import *

# Create your views here.

def default(request):
    loggeado = False
    if request.user.is_authenticated:
        loggeado = True
    return render(request, 'main/base.html', {'loggeado': loggeado})

def home(request):
    loggeado = False
    if request.user.is_authenticated:
        loggeado = True
    return render(request, 'main/home.html', {'loggeado': loggeado})

def loginUser(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if(form.is_valid()):
                
                email = request.POST[Constantes.CLIENTE_EMAIL]
                password = request.POST[Constantes.CLIENTE_PASSWORD]
    
                usuario = authenticate(email=email, password=password)
    
                login(request, usuario)
                return redirect('home')
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {"form": form})

def registerUser(request):


    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if(form.is_valid()):
            
            email = request.POST[Constantes.CLIENTE_EMAIL]
            username = request.POST[Constantes.CLIENTE_USUARIO]
            password = request.POST[Constantes.CLIENTE_PASSWORD]
            tienda = request.POST[Constantes.TIENDA]

            usuario = Usuario(email=email, username=username, password=password)
            usuario = daoUsuario.newCliente(usuario)
            daoUsuario.updateTiendaCliente(usuario, int(tienda))
            return redirect('loginUser')
        
        return render(request, 'registration/register.html', {"form": form})

        
        
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {"form": form})
    
def logout_view(request):
    logout(request)
    return redirect('home')