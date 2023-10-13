from gameheaven.models import Videojuego as Videojuego
from gameheaven.models import Consola as Consola

def newVideojuego(videojuego):
    videojuego.save()
    
def newConsola(consola):
    consola.save()
    
def getVideojuegos():
    return Videojuego.objects.all()

def getConsolas():
    return Consola.objects.all()

def getVideojuego(id):
    return Videojuego.objects.get(id=id)

def getConsola(id):
    return Consola.objects.get(id=id)

    
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
    videojuego.img = imagen
    videojuego.save()
    
def updateImagenConsola(consola, imagen):
    consola.img = imagen
    consola.save()
    
def updateVideojuego(idvideojuego, newVideojuego):
    videojuego = getVideojuego(idvideojuego)
    videojuego.nombre = newVideojuego.nombre
    videojuego.descripcion = newVideojuego.descripcion
    videojuego.img = newVideojuego.img
    videojuego.save()
    
def updateConsola(idConsola, newConsola):
    consola = getConsola(idConsola)
    consola.nombre = newConsola.nombre
    consola.descripcion = newConsola.descripcion
    consola.img = newConsola.img
    consola.save()
    

def deleteVideojuego(videojuego):
    videojuego.delete()

def deleteConsola(consola):
    consola.delete()