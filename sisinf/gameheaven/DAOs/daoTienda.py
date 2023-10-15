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

def getCiudadTienda(idTienda):
    return getTienda(idTienda).ciudad

def getCodigoPostalTienda(idTienda):
    return getTienda(idTienda).codigoPostal

def getVideojuegosTienda(idTienda):
    return getTienda(idTienda).videojuegos

def getConsolasTienda(idTienda):
    return getTienda(idTienda).consolas

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

def getStockConsola(idTienda, idConsola):
    return StockConsola.objects.get(tienda_id=idTienda, consola_id=idConsola)
    
def getTiendaStockConsola(idStockConsola):
    return getStockConsola(idStockConsola).tienda

def getConsolaStockConsola(idStockConsola):
    return getStockConsola(idStockConsola).consola

def getPrecioStockConsola(idStockConsola):
    return getStockConsola(idStockConsola).precio

def getStockStockConsola(idStockConsola):
    return getStockConsola(idStockConsola).stock

#UPDATES

def updateStockConsola(stockConsola, newStockConsola):
    if isinstance(stockConsola, int):
        stockConsola = getStockConsola(stockConsola)
    stockConsola.tienda = newStockConsola.tienda
    stockConsola.consola = newStockConsola.consola
    stockConsola.precio = newStockConsola.precio
    stockConsola.stock = newStockConsola.stock
    stockConsola.save()

def updateTiendaStockConsola(stock, tienda):
    if isinstance(stock, int):
        stock = getStockConsola(stock)
    if isinstance(tienda, int):
        tienda = getTienda(tienda)
    stock.tienda = tienda
    stock.save()

def updateConsolaStockConsola(stock, consola):
    if isinstance(stock, int):
        stock = getStockConsola(stock)
    if isinstance(consola, int):
        consola = daoProductos.getConsola(consola)
    stock.idConsola = consola
    stock.save()

def updatePrecioStockConsola(stock, precio):
    if isinstance(stock, int):
        stock = getStockConsola(stock)
    stock.precio = precio
    stock.save()

def updateStockStockConsola(stock, cantidad):
    if isinstance(stock, int):
        stock = getStockConsola(stock)
    stock.stock = cantidad
    stock.save()

#DELETES

def deleteStockConsola(stockConsola):
    if isinstance(stockConsola, int):
        stockConsola = getStockConsola(stockConsola)
    stockConsola.delete()


### Daos StockVideojuego

def newStockVideojuego(stockVideojuego):
    StockVideojuego.save(stockVideojuego)

#GETTERS (with ID)

def getAllStockVideojuegos():
    return StockVideojuego.objects.all()

def getStockVideojuego(idTienda, idVideojuego):
    return StockVideojuego.objects.get(tienda_id=idTienda, videojuego_id=idVideojuego)

def getIdTiendaStockVideojuego(idStockVideojuego):
    return getStockVideojuego(idStockVideojuego).tienda

def getIdVideojuegoStockVideojuego(idStockVideojuego):
    return getStockVideojuego(idStockVideojuego).videojuego

def getPrecioStockVideojuego(idStockVideojuego):
    return getStockVideojuego(idStockVideojuego).precio

def getStockStockVideojuego(idStockVideojuego):
    return getStockVideojuego(idStockVideojuego).stock

def getStockVideojuegoTienda(idTienda):
    return Tienda.objects.filter(idTienda=idTienda).videojuegos

#UPDATES

def updateStockVideojuego(idStockVideojuego, newStockVideojuego):
    stockVideojuego = getStockVideojuego(idStockVideojuego)
    stockVideojuego.tienda = newStockVideojuego.tienda
    stockVideojuego.videojuego = newStockVideojuego.videojuego
    stockVideojuego.precio = newStockVideojuego.precio
    stockVideojuego.stock = newStockVideojuego.stock
    stockVideojuego.save()

def updateTiendaStockVideojuego(stock, tienda):
    if isinstance(stock, int):
        stock = getStockVideojuego(stock)
    if isinstance(tienda, int):
        tienda = getTienda(tienda)
    stock.idTienda = tienda
    stock.save()

def updateVideojuegoStockVideojuego(stock, videojuego):
    if isinstance(stock, int):
        stock = getStockVideojuego(stock)
    if isinstance(videojuego, int):
        videojuego = daoProductos.getVideojuego(videojuego)
    stock.videojuego = videojuego
    stock.save()

def updatePrecioStockVideojuego(stock, precio):
    if isinstance(stock, int):
        stock = getStockVideojuego(stock)
    stock.precio = precio
    stock.save()

def updateStockStockVideojuego(stock, cantidad):
    if isinstance(stock, int):
        stock = getStockVideojuego(stock)
    stock.stock = stock
    stock.save()

#DELETES

def deleteStockVideojuego(stockVideojuego):
    if isinstance(stockVideojuego, int):
        stockVideojuego = getStockVideojuego(stockVideojuego)
    stockVideojuego.delete()
