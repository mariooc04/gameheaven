from gameheaven.models import Videojuego as Videojuego
from gameheaven.models import Consola as Consola

### Daos Videojuego

def newVideojuego(videojuego):
    videojuego.save()

#GETTERS (with ID)

def getAllVideojuegos():
    return Videojuego.objects.all()

def getVideojuego(idVideojuego):
    return Videojuego.objects.get(pk=idVideojuego)
def getVideojuegoByNombre(nombre):
    return Videojuego.objects.get(nombre=nombre)

def getNombreVideojuego(idVideojuego):
    return getVideojuego(idVideojuego).nombre

def getDescripcionVideojuego(idVideojuego):
    return getVideojuego(idVideojuego).descripcion

def getValoracionVideojuego(idVideojuego):
    return getVideojuego(idVideojuego).valoracion

def getPlataformasVideojuego(idVideojuego):
    return getVideojuego(idVideojuego).plataformas

def getImagenVideojuego(idVideojuego):
    return getVideojuego(idVideojuego).img

#UPDATES

def updateVideojuego(videojuego, newVideojuego):
    if isinstance(videojuego, int):
        videojuego = getVideojuego(videojuego)
    videojuego.nombre = newVideojuego.nombre
    videojuego.descripcion = newVideojuego.descripcion
    videojuego.img = newVideojuego.img
    videojuego.save()

def updateNombreVideojuego(videojuego, nombre):
    if isinstance(videojuego, int):
        videojuego = getVideojuego(videojuego)
    videojuego.nombre = nombre
    videojuego.save()

def updateDescripcionVideojuego(videojuego, descripcion):
    if isinstance(videojuego, int):
        videojuego = getVideojuego(videojuego)
    videojuego.descripcion = descripcion
    videojuego.save()

def updateValoracionVideojuego(videojuego, valoracion):
    if isinstance(videojuego, int):
        videojuego = getVideojuego(videojuego)
    videojuego.valoracion = valoracion
    videojuego.save()

def updatePlataformasVideojuego(videojuego, plataformas):
    if isinstance(videojuego, int):
        videojuego = getVideojuego(videojuego)
    videojuego.plataformas = plataformas
    videojuego.save()

def updateImagenVideojuego(videojuego, imagen):
    if isinstance(videojuego, int):
        videojuego = getVideojuego(videojuego)
    videojuego.img = imagen
    videojuego.save()

#DELETES

def deleteVideojuego(videojuego):
    if isinstance(videojuego, int):
        videojuego = getVideojuego(videojuego)
    videojuego.delete()


### Daos consola
    
def newConsola(consola):
    consola.save()
    
#GETTERS (with ID)

def getAllConsolas():
    return Consola.objects.all()

def getConsola(idConsola):
    return Consola.objects.get(pk=idConsola)
def getConsolaByNombre(nombre):
    return Consola.objects.get(nombre=nombre)

def getNombreConsola(idConsola):
    return getConsola(idConsola).nombre

def getDescripcionConsola(idConsola):
    return getConsola(idConsola).descripcion

def getValoracionConsola(idConsola):
    return getConsola(idConsola).valoracion

def getImagenConsola(idConsola):
    return getConsola(idConsola).img


#UPDATES

def updateConsola(consola, newConsola):
    if isinstance(consola, int):
        consola = getConsola(consola)
    consola.nombre = newConsola.nombre
    consola.descripcion = newConsola.descripcion
    consola.img = newConsola.img
    consola.save()
    
def updateNombreConsola(consola, nombre):
    if isinstance(consola, int):
        consola = getConsola(consola)    
    consola.nombre = nombre
    consola.save()
    
def updateDescripcionConsola(consola, descripcion):
    if isinstance(consola, int):
        consola = getConsola(consola)
    consola.descripcion = descripcion
    consola.save()

def updateValoracionConsola(consola, valoracion):
    if isinstance(consola, int):
        consola = getConsola(consola)
    consola.valoracion = valoracion
    consola.save()
     
def updateImagenConsola(consola, imagen):
    if isinstance(consola, int):
        consola = getConsola(consola)
    consola.img = imagen
    consola.save()

#DELETES

def deleteConsola(consola):
    if isinstance(consola, int):
        consola = getConsola(consola)
    consola.delete()