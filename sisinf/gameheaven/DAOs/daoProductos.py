from gameheaven.models import Videojuego as Videojuego
from gameheaven.models import Consola as Consola

### Daos videojuego

def newVideojuego(videojuego):
    videojuego.save()

def getVideojuegos():
    return Videojuego.objects.all()

def getVideojuego(id):
    return Videojuego.objects.get(pk=id)

def getNombreVideojuego(id):
    return getVideojuego(id).nombre

def getDescripcionVideojuego(id):
    return getVideojuego(id).descripcion

def getImagenVideojuego(id):
    return getVideojuego(id).img

def updateVideojuego(idVideojuego, newVideojuego):
    videojuego = getVideojuego(idVideojuego)
    videojuego.nombre = newVideojuego.nombre
    videojuego.descripcion = newVideojuego.descripcion
    videojuego.img = newVideojuego.img
    videojuego.save()

def updateNombreVideojuego(videojuego, nombre):
    videojuego.nombre = nombre
    videojuego.save()

def updateDescripcionVideojuego(videojuego, descripcion):
    videojuego.descripcion = descripcion
    videojuego.save()

def updateImagenVideojuego(videojuego, imagen):
    videojuego.img = imagen
    videojuego.save()

def deleteVideojuego(videojuego):
    videojuego.delete()


### Daos consola
    
def newConsola(consola):
    consola.save()
    
def getConsolas():
    return Consola.objects.all()

def getConsola(id):
    return Consola.objects.get(id=id)

def getNombreConsola(id):
    return getConsola(id).nombre

def getDescripcionConsola(id):
    return getConsola(id).descripcion

def getImagenConsola(id):
    return getConsola(id).img

def updateConsola(idConsola, newConsola):
    consola = getConsola(idConsola)
    consola.nombre = newConsola.nombre
    consola.descripcion = newConsola.descripcion
    consola.img = newConsola.img
    consola.save()
    
def updateNombreConsola(consola, nombre):
    consola.nombre = nombre
    consola.save()
    
def updateDescripcionConsola(consola, descripcion):
    consola.descripcion = descripcion
    consola.save()
     
def updateImagenConsola(consola, imagen):
    consola.img = imagen
    consola.save()
        
def deleteConsola(consola):
    consola.delete()