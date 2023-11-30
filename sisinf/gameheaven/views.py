from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from gameheaven.models import Cliente, Tienda, Usuario, Consola, Videojuego, ReservaConsola, ReservaVideojuego, StockConsola, StockVideojuego
from gameheaven.Constantes import ConstantesVOs as Constantes
from gameheaven.DAOs import daoUsuario
from gameheaven.DAOs import daoTienda ,daoProductos, daoReserva
from django.contrib.auth import authenticate, login, logout
from gameheaven.forms import RegisterForm, LoginForm, AddShopForm, ConsoleFilterForm
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
from steam import Steam
from decouple import config
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect

urlGETListSteamAPI = "http://api.steampowered.com/ISteamApps/GetAppList/v2"

KEY = config("STEAM_API_KEY")


steam = Steam(KEY)



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
def homeFilter(request):  
    form = ConsoleFilterForm(request.POST)
    if form.is_valid():
        try:
            ps5 = request.POST['PS5']
            ps5 = True
        except:
            ps5 = False
        try:
            xbox = request.POST['XBOX']
            xbox = True
        except:
            xbox = False
        try:
            switch = request.POST['SWITCH']
            switch = True
        except:
            switch = False
        try:
            pc = request.POST['PC']
            pc = True
        except:
            pc = False
        try:
            ps4= request.POST['PS4']
            ps4 = True
        except:
            ps4 = False

        usuario = request.user
        if usuario.role == Usuario.Roles.CLIENTE:
            tienda = daoUsuario.getClienteByUsuario(usuario).tienda
        elif usuario.role == Usuario.Roles.TRABAJADOR:
            tienda = daoUsuario.getTrabajadorByUsuario(usuario).tienda
        elif usuario.role == Usuario.Roles.ADMIN:
            tienda = daoTienda.getRandomTienda()
        consolas = []
        videojuegos = []
        if ps5:
            videojuegos = list(daoProductos.getVideojuegoByPlataforma('PS5'))
        if ps4:
            videojuegos += list(daoProductos.getVideojuegoByPlataforma('PS4'))
        if  pc:
            videojuegos += list(daoProductos.getVideojuegoByPlataforma('PC'))
        if xbox:
            videojuegos += list(daoProductos.getVideojuegoByPlataforma('XBOX'))
        if switch:
            videojuegos += list(daoProductos.getVideojuegoByPlataforma('SWITCH'))
        if (not ps5 and not ps4 and not pc and not xbox and not switch):
            videojuegos += list(daoProductos.getAllVideojuegos())
            consolas += list(daoProductos.getAllConsolas())
        if pc == True:
            print("PC")
        elif ps5 == True:
            print("PS5")
        elif ps4 == True:
            print("PS4")
        elif xbox == True:
            print("XBOX")
        elif switch == True:
            print("SWITCH")
        else:
            print("NADA")
        productos = videojuegos + consolas
        for producto in productos:
            if isinstance(producto, Videojuego) and producto.steamID == None :
                producto.img = base64.b64encode(producto.img).decode('utf-8')
        productosCaro = productos.copy()
        productosBarato = productos.copy()
        for productoCaro in productosCaro:
            if(isinstance(productoCaro, Videojuego)):
                productoCaro.precio = daoTienda.getPrecioStockVideojuego(tienda, productoCaro)
            else:
                productoCaro.precio = daoTienda.getPrecioStockConsola(tienda, productoCaro)
        
        productosCaro = sorted(productosCaro, key=lambda x: x.precio , reverse=True)
        productosBarato = sorted(productosBarato, key=lambda x: x.precio)
        context = {
            'loggeado' : request.user.is_authenticated,
            'currentView' : 'home',
            'productos' : productos,
            'productosCaro' : productosCaro,
            'productosBarato' : productosBarato,
            'tienda' : tienda,
            'form' : form,
        }
    else: #No se si funciona GG
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
            if isinstance(producto, Videojuego) and producto.steamID == None :
                producto.img = base64.b64encode(producto.img).decode('utf-8')
        productosCaro = productos.copy()
        productosBarato = productos.copy()
        for productoCaro in productosCaro:
            if(isinstance(productoCaro, Videojuego)):
                productoCaro.precio = daoTienda.getPrecioStockVideojuego(tienda, productoCaro)
            else:
                productoCaro.precio = daoTienda.getPrecioStockConsola(tienda, productoCaro)
        
        productosCaro = sorted(productosCaro, key=lambda x: x.precio , reverse=True)
        productosBarato = sorted(productosBarato, key=lambda x: x.precio)
        context = {
            'loggeado' : request.user.is_authenticated,
            'currentView' : 'home',
            'productos' : productos,
            'productosCaro' : productosCaro,
            'productosBarato' : productosBarato,
            'tienda' : tienda,
            'form' : form,
        }
    return render(request, 'main/home.html', context)


@login_required(login_url='loginUser')
def home(request):
    form = ConsoleFilterForm(request.POST)
    if form.is_valid():
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
            if isinstance(producto, Videojuego) and producto.steamID == None:
                producto.img = base64.b64encode(producto.img).decode('utf-8')
            elif isinstance(producto, Consola):
                producto.img = base64.b64encode(producto.img).decode('utf-8')
        productosCaro = productos.copy()
        productosBarato = productos.copy()
        for productoCaro in productosCaro:
            if(isinstance(productoCaro, Videojuego)):
                productoCaro.precio = daoTienda.getPrecioStockVideojuego(tienda, productoCaro)
            else:
                productoCaro.precio = daoTienda.getPrecioStockConsola(tienda, productoCaro)
        
        productosCaro = sorted(productosCaro, key=lambda x: x.precio , reverse=True)
        productosBarato = sorted(productosBarato, key=lambda x: x.precio)
        context = {
            'loggeado' : request.user.is_authenticated,
            'currentView' : 'home',
            'productos' : productos,
            'productosCaro' : productosCaro,
            'productosBarato' : productosBarato,
            'tienda' : tienda,
            'form' : form,
        }
    else:
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
        productosCaro = productos.copy()
        for producto in productos:
            if isinstance(producto, Videojuego) and producto.steamID == None:
                producto.img = base64.b64encode(producto.img).decode('utf-8')
        productosCaro = productos.copy()
        productosBarato = productos.copy()
        for productoCaro in productosCaro:
            if(isinstance(productoCaro, Videojuego)):
                productoCaro.precio = daoTienda.getPrecioStockVideojuego(tienda, productoCaro)
            else:
                productoCaro.precio = daoTienda.getPrecioStockConsola(tienda, productoCaro)
        
        productosCaro = sorted(productosCaro, key=lambda x: x.precio , reverse=True)
        productosBarato = sorted(productosBarato, key=lambda x: x.precio)
        context = {
            'loggeado' : request.user.is_authenticated,
            'currentView' : 'home',
            'productos' : productos,
            'productosCaro' : productosCaro,
            'productosBarato' : productosBarato,
            'tienda' : tienda,
            'form' : form,
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
            #valoracion = request.POST['valoracion']
            plataformas = request.POST['plataformas']
            imagen = request.FILES['img'].file.read()
            precio = request.POST['precio']
            producto = Videojuego(nombre=nombre, 
            descripcion=descripcion, plataformas = plataformas, img=imagen)
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

def buscarVideojuegoSteam(request):
    if request.method == 'POST':
        form = BuscardorSteamForm(request.POST)
        nombre = request.POST['nombre']
        games = steam.apps.search_games(nombre)
        
        for app in games['apps']:
            respuesta = steam.apps.get_app_details(app['id'], filters='metacritic')
            respuesta2 = steam.apps.get_app_details(app['id'])
            app['descripcion'] = respuesta2[str(app['id'])]['data']['short_description']
            diccionarioRespuesta = respuesta[str(app['id'])]
            if(diccionarioRespuesta['success'] == False or diccionarioRespuesta['data'] == []):
                app['valoracion'] = 0
            else:
                app['valoracion'] = diccionarioRespuesta['data']['metacritic']['score']
            
            app['price'] = app['price'].replace('$', '')

        print(games)
        
        context = {
            'loggeado' : request.user.is_authenticated,
            'currentView' : 'settings',
            'games' : games,
        }
        return render(request, 'trabajador/steamGames.html', context)
        
    else:
        form = BuscardorSteamForm()
        context = {
            'form' : form,
            'loggeado' : request.user.is_authenticated,
            'currentView' : 'settings',
        }
        return render(request, 'trabajador/buscadorSteam.html', context)

def addVideojuegoSteam(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        precio = request.POST['precio']
        valoracion = request.POST['valoracion']
        steamID = request.POST['steamID']
        
        try:
            imagen = steam.apps.get_app_details(steamID)[str(steamID)]['data']['header_image']
        except:
            imagen = request.POST['imagen']


        #if precio == 'Free to Play' or precio == 'Free To Play' or precio == None or precio == '' or precio == ' ' or precio == 'Free':
        if isinstance(precio, str):
            try:
                precio = float(precio)
            except: 
                precio = 0

        producto = Videojuego(nombre=nombre, 
                            descripcion=descripcion, valoracion=valoracion, steamID=steamID, linkImagen=imagen, plataformas='PC')
        daoProductos.newVideojuego(producto)
        producto = daoProductos.getVideojuegoByNombre(nombre)

        tiendas = daoTienda.getAllTiendas()
        for tienda in tiendas:
            stock = StockVideojuego(tienda = tienda, videojuego = producto, precio = precio, stock = 0)
            daoTienda.newStockVideojuego(stock)
        return redirect('home')

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

@require_POST
@login_required(login_url='loginUser')
@csrf_protect
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
                if(stockVideojuego.stock < 0):
                    stockVideojuego.stock = 0
                stockVideojuego.save()
            except:
                consola = daoProductos.getConsolaByNombre(nombreProducto)
                stockConsola = daoTienda.getStockConsola(tienda, consola)
                stockConsola.stock += stock
                if(stockConsola.stock < 0):
                    stockConsola.stock = 0
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
            if stockConsola.stock == 0:
                return redirect('home')
            reservaConsola = ReservaConsola(cliente=cliente, stockConsola = stockConsola ,fecha=fecha)
            daoReserva.newReservaConsola(reservaConsola)
            stockConsola.stock -= 1
            stockConsola.save()
            return redirect('home')
        elif isinstance (product, Videojuego):
            stockVideojuego = daoTienda.getStockVideojuego(tienda.id, product.id)
            if stockVideojuego.stock == 0:
                return redirect('home')
            reservaVideojuego = ReservaVideojuego(cliente=cliente, stockVideojuego=stockVideojuego, fecha=fecha)
            daoReserva.newReservaVideojuego(reservaVideojuego)
            stockVideojuego.stock -= 1
            stockVideojuego.save()
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
@csrf_protect
def producto(request, product):
    isLink = False
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

    if isinstance(producto, Videojuego) and producto.steamID == None:
        img= base64.b64encode(producto.img).decode('utf-8')
    elif isinstance(producto, Consola):
        img= base64.b64encode(producto.img).decode('utf-8')   
    else:
        img = producto.linkImagen 
        isLink = True

    form = AddStockForm()
    context = {
        'loggeado' : request.user.is_authenticated,
        'stockProducto' : stockProducto,
        'isLink' : isLink,
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
    if request.method == 'POST':        
        idReserva = request.POST['reserva_id']
        isVideojuego = request.POST['isVideojuego']
        if(isVideojuego == 'true'):
            reserva = daoReserva.getReservaVideojuego(idReserva)
        else:
            reserva = daoReserva.getReservaConsola(idReserva)
        reserva.estado = ReservaVideojuego.Estados.COMPLETADA
        reserva.save()
        return redirect('reservas')
