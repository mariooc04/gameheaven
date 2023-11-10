from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from gameheaven.models import Cliente, Tienda, Usuario, Consola, Videojuego, ReservaConsola, ReservaVideojuego, StockConsola, StockVideojuego
from gameheaven.Constantes import ConstantesVOs as Constantes
from gameheaven.DAOs import daoUsuario
from gameheaven.DAOs import daoTienda ,daoProductos, daoReserva
from django.contrib.auth import authenticate, login, logout
from gameheaven.forms import RegisterForm, LoginForm, AddShopForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import permission_required
from django.core.mail import send_mail
import smtplib
import gameheaven.Constantes.ConstantesVOs as Constantes
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from django.utils import timezone
import base64



from .forms import *


from gameheaven.templates import *

# Create your views here.

#Para pruebas, borrar luego
def default(request):
    context = {
        'loggeado' : request.user.is_authenticated,
        'currentView' : 'home'
    }
    return render(request, 'main/base.html', context)

@login_required(login_url='loginUser')
def home(request):   
    usuario = request.user
    if usuario.role == Usuario.Roles.CLIENTE:
        tienda = daoUsuario.getClienteByUsuario(usuario).tienda
    elif usuario.role == Usuario.Roles.TRABAJADOR:
        tienda = daoUsuario.getTrabajadorByUsuario(usuario).tienda
    elif usuario.role == Usuario.Roles.ADMIN:
        tienda = daoTienda.getRandomTienda()
    
    videojuegos = list(daoProductos.getAllVideojuegos())
    consolas = list(daoProductos.getAllConsolas())
    productos = videojuegos + consolas
    for producto in productos:
        producto.img = base64.b64encode(producto.img).decode('utf-8')
    context = {
        'loggeado' : request.user.is_authenticated,
        'currentView' : 'home',
        'productos' : productos,
        'tienda' : tienda,
    }
    return render(request, 'main/home.html', context)

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

    context = {
        'form' : form,
        'loggeado' : request.user.is_authenticated,
        'currentView' : 'login'
    }
    return render(request, 'registration/login.html', context)

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
    else:
        form = RegisterForm()
    
    context = {
        'form' : form,
        'loggeado' : request.user.is_authenticated,
        'currentView' : 'register'
    }
    return render(request, 'registration/register.html', context)

@login_required(login_url='loginUser')
def logout_view(request):
    logout(request)
    return redirect('home')

@login_required(login_url='loginUser')
def settings(request):
    if request.method == 'POST': 
        return redirect('settings')

    context = {
        'loggeado' : request.user.is_authenticated,
        'currentView' : 'settings',
        'userRole' : request.user.role
    }
    return render(request, 'settings.html', context)

@login_required(login_url='loginUser')
def changeTienda(request):
    if request.method == 'POST':
        form = ChangeShopForm(request.POST)

        if(form.is_valid()):
            tienda = request.POST['tienda']
            daoUsuario.updateTiendaCliente(request.user, int(tienda))
            return redirect('settings')
    else:
        form = ChangeShopForm()

    context = {
        'form' : form,
        'loggeado' : request.user.is_authenticated,
        'currentView' : 'settings',
        'userRole' : request.user.role
    }
    return render(request, 'changeTienda.html', context)


@login_required(login_url='loginUser')
@permission_required('gameheaven.add_trabajador', raise_exception=True)
def addTrabajador(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if(form.is_valid()):
            
            email = request.POST[Constantes.CLIENTE_EMAIL]
            username = request.POST[Constantes.CLIENTE_USUARIO]
            password = request.POST[Constantes.CLIENTE_PASSWORD]
            tienda = request.POST[Constantes.TIENDA]

            usuario = daoUsuario.newTrabajador(email, password, username)
            daoUsuario.updateTiendaTrabajador(usuario, int(tienda))
            return redirect('settings')
        
    else:
        form = RegisterForm()

    context = {
        'form' : form,
        'loggeado' : request.user.is_authenticated,
        'currentView' : 'settings'
    }
    return render(request, 'administrador/addTrabajador.html', context)

def about(request):
    context = {
        'loggeado' : request.user.is_authenticated,
        'currentView' : 'about'
    }
    return render(request, 'main/about.html', context)

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
    context = {
        'form' : form,
        'loggeado' : request.user.is_authenticated,
        'currentView' : 'contact'
    }
    return render(request, 'main/contact.html', context)

def addVideojuego(request):
    if request.method == 'POST':
        form = AddVideojuegoForm(request.POST, request.FILES)

        if(form.is_valid()):
            nombre = request.POST['nombre']
            descripcion = request.POST['descripcion']
            valoracion = request.POST['valoracion']
            plataformas = request.POST['plataformas']
            imagen = request.FILES['img'].file.read()
            precio = request.POST['precio']
            producto = Videojuego(nombre=nombre, 
            descripcion=descripcion, plataformas = plataformas, valoracion=valoracion, img=imagen)
            daoProductos.newVideojuego(producto)

            product = daoProductos.getVideojuegoByNombre(nombre)
            tiendas = daoTienda.getAllTiendas()
            for tienda in tiendas:
                stock = StockVideojuego(tienda = tienda, videojuego = product, precio = precio, stock = 0)
                daoTienda.newStockVideojuego(stock)
            return redirect('home')
    else:
        form = AddVideojuegoForm()
        
    context = {
        'form' : form,
        'loggeado' : request.user.is_authenticated,
        'currentView' : 'settings',
        'videojuego' : True
    }
    return render(request, 'trabajador/addProduct.html', context)

def addConsola(request):
    if request.method == 'POST':
        form = AddConsolaForm(request.POST, request.FILES)

        if(form.is_valid()):
            nombre = request.POST['nombre']
            descripcion = request.POST['descripcion']
            valoracion = request.POST['valoracion']
            imagen = request.FILES['img'].file.read()
            precio = request.POST['precio']

            producto = Consola(nombre=nombre, 
                               descripcion=descripcion, valoracion=valoracion, img=imagen)
            daoProductos.newConsola(producto)
            producto = daoProductos.getConsolaByNombre(nombre)

            tiendas = daoTienda.getAllTiendas()
            for tienda in tiendas:
                stock = StockConsola(tienda = tienda, consola = producto, precio = precio, stock = 0)
                daoTienda.newStockConsola(stock)
            return redirect('home')
    else:
        form = AddConsolaForm()
        
    context = {
        'form' : form,
        'loggeado' : request.user.is_authenticated,
        'currentView' : 'settings',
        'videojuego' : False
    }
    return render(request, 'trabajador/addProduct.html', context)

@login_required(login_url='loginUser')
def addStockProduct(request):
    if request.method == 'POST':
        form = AddStockForm(request.POST)

        if(form.is_valid()):
            
            nombreProducto = request.POST['nombreProducto']
            stock = int(request.POST['stock'])
            trabajador = daoUsuario.getTrabajadorByUsuario(request.user.id)
            tienda = trabajador.tienda
            try: 
                videojuego = daoProductos.getVideojuegoByNombre(nombreProducto)
                stockVideojuego = daoTienda.getStockVideojuego(tienda, videojuego)
                stockVideojuego.stock += stock
                stockVideojuego.save()
            except:
                consola = daoProductos.getConsolaByNombre(nombreProducto)
                stockConsola = daoTienda.getStockConsola(tienda, consola)
                stockConsola.stock += stock
                stockConsola.save()

            return redirect('producto/' + nombreProducto)
        
    return redirect('home')

    

@login_required(login_url='loginUser')
def addReserva(request, nombre):
    if request.user.role == Usuario.Roles.CLIENTE:
        usuario = request.user
        cliente = daoUsuario.getClienteByUsuario(usuario.id)
        tienda = cliente.tienda
        fecha = timezone.now().date()
    

        try:
            product = daoProductos.getConsolaByNombre(nombre)
        except:
            product = daoProductos.getVideojuegoByNombre(nombre)


        if isinstance (product, Consola):
            stockConsola = daoTienda.getStockConsola(tienda.id, product.id)
            reservaConsola = ReservaConsola(cliente=cliente, stockConsola = stockConsola ,fecha=fecha)
            daoReserva.newReservaConsola(reservaConsola)
            return redirect('home')
        elif isinstance (product, Videojuego):
            stockVideojuego = daoTienda.getStockVideojuego(tienda.id, product.id)
            reservaVideojuego = ReservaVideojuego(cliente=cliente, stockVideojuego=stockVideojuego, fecha=fecha)
            daoReserva.newReservaVideojuego(reservaVideojuego)
    return redirect('home')



        
        

@login_required(login_url='loginUser')
def verReservas(request):
    usuario = request.user
    
    if request.user.role == Usuario.Roles.CLIENTE:
        reservasConsola = daoReserva.filterReservasConsolaByCliente(usuario.id)
        reservasVideojuego = daoReserva.filterReservasVideojuegoByCliente(usuario.id)

        context = {
            'userRole' : request.user.role,
            'reservasConsola': reservasConsola,
            'reservasVideojuego' : reservasVideojuego,
            'loggeado' : request.user.is_authenticated,
            'currentView' : 'home'
        }
        return render(request, 'reservas.html', context)
    elif request.user.role == 'TRABAJADOR':
        reservasConsola = daoReserva.getAllReservasConsola
        reservasVideojuego = daoReserva.getAllReservasVideojuego
        context = {
            'userRole' : request.user.role,
            'reservasConsola': reservasConsola,
            'reservasVideojuego' : reservasVideojuego,
            'loggeado' : request.user.is_authenticated,
            'currentView' : 'home'
        }
        return render(request, 'reservas.html', context)

    context = {
        'userRole' : request.user.role,
        'loggeado' : request.user.is_authenticated,
        'currentView' : 'home'
    }
    return render(request, 'reservas.html', context)

@login_required(login_url='loginUser')
@permission_required('gameheaven.add_usuario', raise_exception=True)
def gestionarTrabajadores(request):
    trabajadores = daoUsuario.getAllTrabajadores()

    context = {
        'trabajadores' : trabajadores,
        'loggeado' : request.user.is_authenticated,
        'currentView' : 'settings'
    }
    return render(request, 'administrador/gestionarTrabajadores.html', 
                context)

@login_required(login_url='loginUser')
def deleteMyAccount(request,id):
    user = daoUsuario.getUsuario(id)
    daoUsuario.deleteUser(user)
    logout(request)
    return redirect('home')

@login_required(login_url='loginUser')
@permission_required('gameheaven.delete_usuario', raise_exception=True)
def deleteTrabajador(request, id):
    user = daoUsuario.getUsuario(id)
    daoUsuario.deleteUser(user)
    return redirect('gestionarTrabajadores')


@login_required(login_url='loginUser')
@permission_required('gameheaven.add_tienda', raise_exception=True)
def gestionarTiendas(request):
    tiendas = daoTienda.getAllTiendas()
    context = {
        'tiendas' : tiendas,
        'loggeado' : request.user.is_authenticated
    }
    return render(request, 'administrador/gestionarTiendas.html',context)

@login_required(login_url='loginUser')
@permission_required('gameheaven.delete_tienda', raise_exception=True)
def delete_shop(request, idTienda):
    daoTienda.deleteTienda(idTienda)
    return redirect('gestionarTiendas')


#--------PRODUCTO----------
@login_required(login_url='loginUser')
def producto(request, product):
    videojuego = False
    try: 
        usuario = daoUsuario.getClienteByUsuario(request.user)
    except:
        usuario = daoUsuario.getTrabajadorByUsuario(request.user)

    try: 
        producto = daoProductos.getConsolaByNombre(product)
        stockProducto = daoTienda.getStockConsola(usuario.tienda, producto.id)
    except:
        producto = daoProductos.getVideojuegoByNombre(product)
        stockProducto = daoTienda.getStockVideojuego(usuario.tienda, producto.id)
        videojuego = True
    img= base64.b64encode(producto.img).decode('utf-8')

    form = AddStockForm()
    context = {
        'loggeado' : request.user.is_authenticated,
        'stockProducto' : stockProducto,
        'currentView' : 'home',
        'img' : img,
        'form' : form,
        }
    
    return render(request,'producto/producto.html', context)

@login_required(login_url='loginUser')
@permission_required('gameheaven.add_tienda', raise_exception=True)
def add_shop(request):
    if request.method == 'POST':
        form = AddShopForm(request.POST)

        if(form.is_valid()):
            ciudad = request.POST['ciudad']
            codigoPostal = request.POST['codigoPostal']
            tienda = Tienda(ciudad=ciudad, codigoPostal=codigoPostal)
            daoTienda.newTienda(tienda)
            return redirect('gestionarTiendas')
         
    form = AddShopForm()

    context = {
        'form' : form,
        'loggeado' : request.user.is_authenticated,
        }
    
    return render(request, 'administrador/addShop.html', context)


@login_required(login_url='loginUser')
def completeReserva(request):
    redirect('home')