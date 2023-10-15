from gameheaven.models import Videojuego as Videojuego
from gameheaven.models import Consola as Consola

### Daos Videojuego

def newVideojuego(videojuego):
    videojuego.save()



def getAllVideojuegos():
    return Videojuego.objects.all()

def getVideojuego(idVideojuego):
    return Videojuego.objects.get(pk=idVideojuego)

def getNombreVideojuego(idVideojuego):
    return getVideojuego(idVideojuego).nombre

def getDescripcionVideojuego(id):
    return getVideojuego(id).descripcion

def getValoracionVideojuego(idVideojuego):
    return getVideojuego(idVideojuego).valoracion

def getPlataformasVideojuego(idVideojuego):
    return getVideojuego(idVideojuego).plataformas

def getImagenVideojuego(id):
    return getVideojuego(id).img



def updateVideojuego(idVideojuego, newVideojuego):
    videojuego = getVideojuego(idVideojuego)
    videojuego.nombre = newVideojuego.nombre
    videojuego.descripcion = newVideojuego.descripcion
    videojuego.img = newVideojuego.img
    videojuego.save()

def updateNombreVideojuego(idVideojuego, nombre):
    videojuego = getVideojuego(idVideojuego)
    videojuego.nombre = nombre
    videojuego.save()

def updateDescripcionVideojuego(idVideojuego, descripcion):
    videojuego = getVideojuego(idVideojuego)
    videojuego.descripcion = descripcion
    videojuego.save()

def updateValoracionVideojuego(idVideojuego, valoracion):
    videojuego = getVideojuego(idVideojuego)
    videojuego.valoracion = valoracion
    videojuego.save()

def updatePlataformasVideojuego(idVideojuego, plataformas):
    videojuego = getVideojuego(idVideojuego)
    videojuego.plataformas = plataformas
    videojuego.save()

def updateImagenVideojuego(idVideojuego, imagen):
    videojuego = getVideojuego(idVideojuego)
    videojuego.img = imagen
    videojuego.save()

def deleteVideojuego(videojuego):
    if isinstance(videojuego, int):
        videojuego = getVideojuego(videojuego)
    videojuego.delete()


### Daos consola
    
def newConsola(consola):
    consola.save()
    


def getAllConsolas():
    return Consola.objects.all()

def getConsola(idConsola):
    return Consola.objects.get(pk=idConsola)

def getNombreConsola(idConsola):
    return getConsola(idConsola).nombre

def getDescripcionConsola(idConsola):
    return getConsola(idConsola).descripcion

def getValoracionConsola(idConsola):
    return getConsola(idConsola).valoracion

def getImagenConsola(id):
    return getConsola(id).img



def updateConsola(idConsola, newConsola):
    consola = getConsola(idConsola)
    consola.nombre = newConsola.nombre
    consola.descripcion = newConsola.descripcion
    consola.img = newConsola.img
    consola.save()
    
def updateNombreConsola(idConsola, nombre):
    consola = getConsola(idConsola)
    consola.nombre = nombre
    consola.save()
    
def updateDescripcionConsola(idConsola, descripcion):
    consola = getConsola(idConsola)
    consola.descripcion = descripcion
    consola.save()

def updateValoracionConsola(idConsola, valoracion):
    consola = getConsola(idConsola)
    consola.valoracion = valoracion
    consola.save()
     
def updateImagenConsola(idConsola, imagen):
    consola = getConsola(idConsola)
    consola.img = imagen
    consola.save()
        
def deleteConsola(consola):
    if isinstance(consola, int):
        consola = getConsola(consola)
    consola.delete()