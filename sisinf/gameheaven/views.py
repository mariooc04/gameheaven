from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from gameheaven.models import Cliente, Tienda, Usuario, Consola, Videojuego
from gameheaven.Constantes import ConstantesVOs as Constantes
from gameheaven.DAOs import daoUsuario
from gameheaven.DAOs import daoTienda ,daoProductos
from django.contrib.auth import authenticate, login, logout
from gameheaven.forms import RegisterForm, LoginForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import permission_required
from django.core.mail import send_mail
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import base64



from .forms import *


from gameheaven.templates import *

# Create your views here.

#Para pruebas, borrar luego
def default(request):
    loggeado = False
    if request.user.is_authenticated:
        loggeado = True
    return render(request, 'main/base.html', {'loggeado': loggeado})

def home(request):
    loggeado = False
    if request.user.is_authenticated:
        loggeado = True
    productos = daoProductos.getAllVideojuegos()
    for producto in productos:
        producto.img = base64.b64encode(producto.img).decode('utf-8')
    return render(request, 'main/home.html', {'loggeado': loggeado, 'productos': productos})

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

@login_required(login_url='loginUser')
def logout_view(request):
    logout(request)
    return redirect('home')

@login_required(login_url='loginUser')
def settings(request):
    usuario = request.user
    if request.method == 'POST':
        form = changeTienda(request.POST)
        tienda = request.POST[Constantes.TIENDA]

        daoUsuario.updateTiendaCliente(usuario, int(tienda))
        return redirect('settings')
    else:
        form = changeTienda(initial={'tienda': daoUsuario.getClienteByUsuario(usuario).tienda})
        
    return render(request, 'settings.html', {'userRole': request.user.role, 'form': form})

@login_required(login_url='loginUser')
def delete_account(request):
    user = request.user
    daoUsuario.deleteUser(user)
    logout(request)
    return redirect('home')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    if request.method == 'POST':
        form = SendEmailForm(request.POST)

        if(form.is_valid()):
            #TODO: REVISAR, NO FUNCIONA
            smtp_server = 'smtp.gmail.com'
            port = 587
            smtp_username = 'gameheaven.adm@gmail.com'
            smtp_password = 'gameheaven.administrator1234'

            fromEmail = request.POST['email']
            subject = request.POST['subject']
            body = "Mensaje enviado por: " + fromEmail + "\n" + request.POST['message']

            msg = MIMEMultipart()
            msg['Subject'] = subject
            msg['From'] = smtp_username
            msg['To'] = smtp_username
            msg.attach(MIMEText(body, 'plain'))

            with smtplib.SMTP(smtp_server, port) as server:
                server.starttls()
                server.login(smtp_username, smtp_password)
                server.sendmail(smtp_username, smtp_username, msg.as_string())
                server.quit()

    else:
        form = SendEmailForm()

    return render(request, 'main/contact.html', {"form": form})

def addproduct(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)

        if(form.is_valid()):
            nombre = request.POST['nombre']
            descripcion = request.POST['descripcion']
            valoracion = request.POST['valoracion']
            plataformas = request.POST['plataformas']
            imagen = request.FILES['img'].file.read()
            if plataformas == None:
                producto = Consola(nombre=nombre, descripcion=descripcion, valoracion=valoracion, img=imagen)
                daoProductos.newConsola(producto)
            else:
                producto = Videojuego(nombre=nombre, descripcion=descripcion, plataformas = plataformas, valoracion=valoracion, img=imagen)
                daoProductos.newVideojuego(producto)
            return redirect('home')
    else:
        form = AddProductForm()
    return render(request, 'trabajador/addproduct.html', {"form": form})
