from gameheaven.models import Tienda as Tienda
from gameheaven.models import StockConsola as StockConsola
from gameheaven.models import StockVideojuego as StockVideojuego
from gameheaven.DAOs import daoProductos as daoProductos

### Daos Tienda

def newTienda(tienda):
    tienda.save()


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



def addConsolaTienda(tienda, consola, precio, stock):
    stockConsolas = StockConsola(tienda=tienda, consola=consola, precio=precio, stock=stock)
    stockConsolas.save()

def addVideojuegoTienda(tienda, videojuego, precio, stock):
    stockVideojuego = StockVideojuego(tienda=tienda, videojuego=videojuego, precio=precio, stock=stock)
    stockVideojuego.save()

def removeConsolaTienda(idTienda, idConsola):
    tienda = getTienda(idTienda)
    consola = daoProductos.getConsola(idConsola)
    tienda.consolas.remove(consola)

def removeVideojuegoTienda(idTienda, idVideojuego):
    tienda = getTienda(idTienda)
    videojuego = daoProductos.getVideojuego(idVideojuego)
    tienda.videojuegos.remove(videojuego)



def deleteTienda(idTienda):
    tienda = getTienda(idTienda)
    tienda.delete()





### Daos StockConsola

def newStockConsola(stockConsola):
    stockConsola.save()


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



def updateStockConsola(idStockConsola, newStockConsola):
    stockConsola = getStockConsola(idStockConsola)
    stockConsola.tienda = newStockConsola.tienda
    stockConsola.consola = newStockConsola.consola
    stockConsola.precio = newStockConsola.precio
    stockConsola.stock = newStockConsola.stock
    stockConsola.save()

def updateTiendaStockConsola(idStockConsola, idTienda):
    stockConsolas = getStockConsola(idStockConsola)
    tienda = getTienda(idTienda)
    stockConsolas.tienda = tienda
    stockConsolas.save()

def updateConsolaStockConsola(idStockConsola, idConsola):
    stockConsolas = getStockConsola(idStockConsola)
    consola = daoProductos.getConsola(idConsola)
    stockConsolas.idConsola = consola
    stockConsolas.save()

def updatePrecioStockConsola(idStockConsola, precio):
    stockConsolas = getStockConsola(idStockConsola)
    stockConsolas.precio = precio
    stockConsolas.save()

def updateStockStockConsola(idStockConsola, stock):
    stockConsolas = getStockConsola(idStockConsola)
    stockConsolas.stock = stock
    stockConsolas.save()



def deleteStockConsola(idStockConsola):
    stockConsola = getStockConsola(idStockConsola)
    stockConsola.delete()


### Daos StockVideojuego

def newStockVideojuego(stockVideojuego):
    StockVideojuego.save(stockVideojuego)



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



def updateStockVideojuego(idStockVideojuego, newStockVideojuego):
    stockVideojuego = getStockVideojuego(idStockVideojuego)
    stockVideojuego.tienda = newStockVideojuego.tienda
    stockVideojuego.videojuego = newStockVideojuego.videojuego
    stockVideojuego.precio = newStockVideojuego.precio
    stockVideojuego.stock = newStockVideojuego.stock
    stockVideojuego.save()

def updateTiendaStockVideojuego(idStockVideojuego, idTienda):
    stockVideojuego = getStockVideojuego(idStockVideojuego)
    tienda = getTienda(idTienda)
    stockVideojuego.idTienda = tienda
    stockVideojuego.save()

def updateVideojuegoStockVideojuego(idStockVideojuego, idVideojuego):
    stockVideojuego = getStockVideojuego(idStockVideojuego)
    videojuego = daoProductos.getVideojuego(idVideojuego)
    stockVideojuego.videojuego = videojuego
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
    stockVideojuego = getStockVideojuego(idStockVideojuego)
    stockVideojuego.delete()
