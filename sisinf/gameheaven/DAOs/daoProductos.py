from models import Videojuego as Videojuego
from models import Consola as Consola

def getVideojuegos():
    return Videojuego.objects.all()

def getConsolas():
    return Consola.objects.all()

def getVideojuegoById(id):
    return Videojuego.objects.get(id=id)

def getConsolaById(id):
    return Consola.objects.get(id=id)

def addVideojuego(videojuego):
    videojuego.save()
    
def addConsola(consola):
    consola.save()
    
def updatePrecioVideojuego(videojuego, precio):
    videojuego.precio = precio
    videojuego.save()
    
def updatePrecioConsola(consola, precio):
    consola.precio = precio
    consola.save()
    
def updateNombreVideojuego(videojuego, nombre):
    videojuego.nombre = nombre
    videojuego.save()
    
def updateNombreConsola(consola, nombre):
    consola.nombre = nombre
    consola.save()
    
def updateDescripcionVideojuego(videojuego, descripcion):
    videojuego.descripcion = descripcion
    videojuego.save()
    
def updateDescripcionConsola(consola, descripcion):
    consola.descripcion = descripcion
    consola.save()
    
def updateImagenVideojuego(videojuego, imagen):
    videojuego.imagen = imagen
    videojuego.save()
    
def updateImagenConsola(consola, imagen):
    consola.imagen = imagen
    consola.save()
    
def updateVideojuego(videojuego, nombre, descripcion, precio, imagen):
    videojuego.nombre = nombre
    videojuego.descripcion = descripcion
    videojuego.precio = precio
    videojuego.imagen = imagen
    videojuego.save()
    
def updateConsola(consola, nombre, descripcion, precio, imagen):
    consola.nombre = nombre
    consola.descripcion = descripcion
    consola.precio = precio
    consola.imagen = imagen
    consola.save()
    

def deleteVideojuego(videojuego):
    videojuego.delete()

def deleteConsola(consola):
    consola.delete()