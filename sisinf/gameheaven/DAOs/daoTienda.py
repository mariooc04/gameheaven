from gameheaven.models import Tienda as Tienda
from gameheaven.models import StockConsolas as StockConsolas
from gameheaven.models import StockVideojuego as StockVideojuego

###Tiendas


def newTienda(tienda):
    Tienda.save(tienda)

def getTienda(idTienda):
    return Tienda.objects.get(pk=idTienda)

def getCodigoPostalTienda(idTienda):
    return Tienda.objects.get(pk=idTienda).codigoPostal

def getCiudadTienda(idTienda):
    return Tienda.objects.get(pk=idTienda).ciudad

def updateTienda(idTienda, newTienda):
    tienda = getTienda(idTienda)
    tienda.ciudad = newTienda.ciudad
    tienda.codigoPostal = newTienda.codigoPostal
    tienda.save()

def updateCodigoPostalTienda(idTienda, codigoPostal):
    tienda = getTienda(idTienda)
    tienda.codigoPostal = codigoPostal
    tienda.save()

def updateCiudadTienda(idTienda, ciudad):
    tienda = getTienda(idTienda)
    tienda.ciudad = ciudad
    tienda.save()

def deleteTienda(idTienda):
    Tienda.objects.get(pk=idTienda).delete()

def addConsolaTienda(tienda, consola, precio, stock):
    stockConsolas = StockConsolas(tienda=tienda, consola=consola, precio=precio, stock=stock)
    stockConsolas.save()

def addVideojuegoTienda(tienda, videojuego, precio, stock):
    stockVideojuego = StockVideojuego(tienda=tienda, videojuego=videojuego, precio=precio, stock=stock)
    stockVideojuego.save()

def removeConsolaTienda(idTienda, idConsola):
    tienda = getTienda(idTienda)
    tienda.consolas.remove(idConsola)
    tienda.save()

def removeVideojuegoTienda(idTienda, idVideojuego):
    tienda = getTienda(idTienda)
    tienda.videojuegos.remove(idVideojuego)
    tienda.save()

###StockConsolas

def newStockConsolas(stockConsolas):
    stockConsolas.save()

def getStockConsola(idTienda, idConsola):
    return StockConsolas.objects.get(tienda_id=idTienda, consola_id=idConsola)
    
def getIdTiendaStockConsolas(idStockConsolas):
    return getStockConsola(idStockConsolas).idTienda

def getIdConsolaStockConsolas(idStockConsolas):
    return getStockConsola(idStockConsolas).idConsola

def getPrecioStockConsolas(idStockConsolas):
    return getStockConsola(idStockConsolas).precio

def getAllStockConsolas(idStockConsolas):
    return getStockConsola(idStockConsolas).stock


def updateStockConsolas(idStockConsolas, newStockConsolas):
    stockConsolas = getStockConsola(idStockConsolas)
    stockConsolas.idTienda = newStockConsolas.idTienda
    stockConsolas.idConsola = newStockConsolas.idConsola
    stockConsolas.precio = newStockConsolas.precio
    stockConsolas.stock = newStockConsolas.stock
    stockConsolas.save()

def updateIdTiendaStockConsolas(idStockConsolas, idTienda):
    stockConsolas = getStockConsola(idStockConsolas)
    stockConsolas.idTienda = idTienda
    stockConsolas.save()

def updateIdConsolaStockConsolas(idStockConsolas, idConsola):
    stockConsolas = getStockConsola(idStockConsolas)
    stockConsolas.idConsola = idConsola
    stockConsolas.save()

def updatePrecioStockConsolas(idStockConsolas, precio):
    stockConsolas = getStockConsola(idStockConsolas)
    stockConsolas.precio = precio
    stockConsolas.save()

def updateStockStockConsolas(idStockConsolas, stock):
    stockConsolas = getStockConsola(idStockConsolas)
    stockConsolas.stock = stock
    stockConsolas.save()


###StockVideojuego

def newStockVideojuego(stockVideojuego):
    StockVideojuego.save(stockVideojuego)

def getStockVideojuego(idTienda, idVideojuego):
    return StockVideojuego.objects.get(tienda_id=idTienda, videojuego_id=idVideojuego)

def getIdTiendaStockVideojuego(idStockVideojuego):
    return getStockVideojuego(idStockVideojuego).idTienda

def getIdVideojuegoStockVideojuego(idStockVideojuego):
    return getStockVideojuego(idStockVideojuego).idVideojuego

def getPrecioStockVideojuego(idStockVideojuego):
    return getStockVideojuego(idStockVideojuego).precio

def getAllStockVideojuego(idStockVideojuego):
    return getStockVideojuego(idStockVideojuego).stock

def getStockVideojuegoTienda(idTienda):
    return Tienda.objects.filter(idTienda=idTienda).videojuegos

def updateStockVideojuego(idStockVideojuego, newStockVideojuego):
    stockVideojuego = getStockVideojuego(idStockVideojuego)
    stockVideojuego.idTienda = newStockVideojuego.idTienda
    stockVideojuego.idVideojuego = newStockVideojuego.idVideojuego
    stockVideojuego.precio = newStockVideojuego.precio
    stockVideojuego.stock = newStockVideojuego.stock
    stockVideojuego.save()

def updateIdTiendaStockVideojuego(idStockVideojuego, idTienda):
    stockVideojuego = getStockVideojuego(idStockVideojuego)
    stockVideojuego.idTienda = idTienda
    stockVideojuego.save()

def updateIdVideojuegoStockVideojuego(idStockVideojuego, idVideojuego):
    stockVideojuego = getStockVideojuego(idStockVideojuego)
    stockVideojuego.idVideojuego = idVideojuego
    stockVideojuego.save()

def updatePrecioStockVideojuego(idStockVideojuego, precio):
    stockVideojuego = getStockVideojuego(idStockVideojuego)
    stockVideojuego.precio = precio
    stockVideojuego.save()

def updateStockStockVideojuego(idStockVideojuego, stock):
    stockVideojuego = getStockVideojuego(idStockVideojuego)
    stockVideojuego.stock = stock
    stockVideojuego.save()
