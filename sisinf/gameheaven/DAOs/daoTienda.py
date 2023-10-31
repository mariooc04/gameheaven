from gameheaven.models import Tienda as Tienda
from gameheaven.models import StockConsola as StockConsola
from gameheaven.models import StockVideojuego as StockVideojuego
from gameheaven.DAOs import daoProductos as daoProductos

### Daos Tienda

def newTienda(tienda):
    tienda.save()

#GETTERS(with ID)

def getAllTiendas():
    return Tienda.objects.all()

def getTienda(idTienda):
    return Tienda.objects.get(pk=idTienda)

def getTiendaByCiudadCodigoPostal(ciudad, codigoPostal):
    return Tienda.objects.get(ciudad=ciudad, codigoPostal=codigoPostal)

def getCiudadTienda(idTienda):
    return getTienda(idTienda).ciudad

def getCodigoPostalTienda(idTienda):
    return getTienda(idTienda).codigoPostal

def getVideojuegosTienda(idTienda):
    return getTienda(idTienda).videojuegos

def getConsolasTienda(idTienda):
    return getTienda(idTienda).consolas

def existeTienda(ciudad, codigoPostal):
    return Tienda.objects.filter(ciudad=ciudad, codigoPostal=codigoPostal).exists()

#UPDATES

def updateTienda(tienda, newTienda):
    if isinstance(tienda, int):
        tienda = getTienda(tienda)
    tienda.ciudad = newTienda.ciudad
    tienda.codigoPostal = newTienda.codigoPostal
    tienda.save()

def updateCodigoPostalTienda(tienda, codigoPostal):
    if isinstance(tienda, int):
        tienda = getTienda(tienda)
    tienda.codigoPostal = codigoPostal
    tienda.save()

def updateCiudadTienda(tienda, ciudad):
    if isinstance(tienda, int):
        tienda = getTienda(tienda)
    tienda.ciudad = ciudad
    tienda.save()

#ADD/REMOVE

def addConsolaTienda(tienda, consola, precio, stock):
    stockConsolas = StockConsola(tienda=tienda, consola=consola, precio=precio, stock=stock)
    stockConsolas.save()

def addVideojuegoTienda(tienda, videojuego, precio, stock):
    stockVideojuego = StockVideojuego(tienda=tienda, videojuego=videojuego, precio=precio, stock=stock)
    stockVideojuego.save()

def removeConsolaTienda(tienda, consola):
    if isinstance(tienda, int):
        tienda = getTienda(tienda)
    if isinstance(consola, int):
        consola = daoProductos.getConsola(consola)
    tienda.consolas.remove(consola)

def removeVideojuegoTienda(tienda, videojuego):
    if isinstance(tienda, int):
        tienda = getTienda(tienda)
    if isinstance(videojuego, int):
        videojuego = daoProductos.getVideojuego(videojuego)
    tienda.videojuegos.remove(videojuego)

#DELETES

def deleteTienda(tienda):
    if isinstance(tienda, int):
        tienda = getTienda(tienda)
    tienda.delete()





### Daos StockConsola

def newStockConsola(stockConsola):
    stockConsola.save()

#GETTERS (with ID)

def getAllStockConsolas():
    return StockConsola.objects.all()

def getStockConsola(tienda, consola):
    return StockConsola.objects.get(tienda=tienda, consola=consola)
    

def getPrecioStockConsola(tienda, consola):
    return getStockConsola(tienda, consola).precio

def getStockStockConsola(tienda, consola):
    return getStockConsola(tienda, consola).stock

#UPDATES

def updateStockConsola(tienda, consola, newStockConsola):
    stockConsola = getStockConsola(tienda, consola)
    stockConsola.precio = newStockConsola.precio
    stockConsola.stock = newStockConsola.stock
    stockConsola.save()



def updatePrecioStockConsola(tienda, consola, precio):
    stockConsola = getStockConsola(tienda, consola)
    stockConsola.precio = precio
    stockConsola.save()

def updateStockStockConsola(tienda, consola, stock):
    stockConsola = getStockConsola(tienda, consola)
    stockConsola.stock = stock
    stockConsola.save()

#DELETES

def deleteStockConsola(tienda, consola):
    stockConsola = getStockConsola(tienda, consola)
    stockConsola.delete()

### Daos StockVideojuego

def newStockVideojuego(stockVideojuego):
    StockVideojuego.save(stockVideojuego)

#GETTERS (with ID)

def getAllStockVideojuegos():
    return StockVideojuego.objects.all()

def getStockVideojuego(tienda, videojuego):
    return StockVideojuego.objects.get(tienda=tienda, videojuego=videojuego)

def getPrecioStockVideojuego(tienda, videojuego):
    return getStockVideojuego(tienda, videojuego).precio

def getStockStockVideojuego(tienda, videojuego):
    return getStockVideojuego(tienda, videojuego).stock


#UPDATES

def updateStockVideojuego(tienda, videojuego, newStockVideojuego):
    stockVideojuego = getStockVideojuego(tienda, videojuego)
    stockVideojuego.precio = newStockVideojuego.precio
    stockVideojuego.stock = newStockVideojuego.stock
    stockVideojuego.save()

def updatePrecioStockVideojuego(tienda, videojuego, precio):
    stockVideojuego = getStockVideojuego(tienda, videojuego)
    stockVideojuego.precio = precio
    stockVideojuego.save()

def updateStockStockVideojuego(tienda, videojuego, stock):
    stockVideojuego = getStockVideojuego(tienda, videojuego)
    stockVideojuego.stock = stock
    stockVideojuego.save()
 
#DELETES

def deleteStockVideojuego(tienda, videojuego):
    stockVideojuego = getStockVideojuego(tienda, videojuego)
    stockVideojuego.delete()
