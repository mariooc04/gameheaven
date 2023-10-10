from models import Tienda as Tienda


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