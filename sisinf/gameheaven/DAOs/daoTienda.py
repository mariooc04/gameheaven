from models import Tienda as Tienda
from models import StockConsolas as StockConsolas
from models import StockVideojuego as StockVideojuego

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

###StockConsolas

def newStockConsolas(stockConsolas):
    stockConsolas.save()

def getStockConsolas(idStockConsolas):
    return StockConsolas.objects.get(pk=idStockConsolas)

def getIdTiendaStockConsolas(idStockConsolas):
    return getStockConsolas(idStockConsolas).idTienda

def getIdConsolaStockConsolas(idStockConsolas):
    return getStockConsolas(idStockConsolas).idConsola

def getPrecioStockConsolas(idStockConsolas):
    return getStockConsolas(idStockConsolas).precio

def getStockStockConsolas(idStockConsolas):
    return getStockConsolas(idStockConsolas).stock

def getStockConsolasTienda(idTienda):
    return Tienda.objects.filter(idTienda=idTienda).consolas

def updateStockConsolas(idStockConsolas, newStockConsolas):
    stockConsolas = getStockConsolas(idStockConsolas)
    stockConsolas.idTienda = newStockConsolas.idTienda
    stockConsolas.idConsola = newStockConsolas.idConsola
    stockConsolas.precio = newStockConsolas.precio
    stockConsolas.stock = newStockConsolas.stock
    stockConsolas.save()

def updateIdTiendaStockConsolas(idStockConsolas, idTienda):
    stockConsolas = getStockConsolas(idStockConsolas)
    stockConsolas.idTienda = idTienda
    stockConsolas.save()

def updateIdConsolaStockConsolas(idStockConsolas, idConsola):
    stockConsolas = getStockConsolas(idStockConsolas)
    stockConsolas.idConsola = idConsola
    stockConsolas.save()

def updatePrecioStockConsolas(idStockConsolas, precio):
    stockConsolas = getStockConsolas(idStockConsolas)
    stockConsolas.precio = precio
    stockConsolas.save()

def updateStockStockConsolas(idStockConsolas, stock):
    stockConsolas = getStockConsolas(idStockConsolas)
    stockConsolas.stock = stock
    stockConsolas.save()

def deleteStockConsolas(idStockConsolas):
    StockConsolas.objects.get(pk=idStockConsolas).delete()

###StockVideojuego

def newStockVideojuego(stockVideojuego):
    StockVideojuego.save(stockVideojuego)

def getStockVideojuego(idStockVideojuego):
    return StockVideojuego.objects.get(pk=idStockVideojuego)

def getIdTiendaStockVideojuego(idStockVideojuego):
    return getStockVideojuego(idStockVideojuego).idTienda

def getIdVideojuegoStockVideojuego(idStockVideojuego):
    return getStockVideojuego(idStockVideojuego).idVideojuego

def getPrecioStockVideojuego(idStockVideojuego):
    return getStockVideojuego(idStockVideojuego).precio

def getStockStockVideojuego(idStockVideojuego):
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

def deleteStockVideojuego(idStockVideojuego):
    StockVideojuego.objects.get(pk=idStockVideojuego).delete()