from gameheaven.models import ReservaConsola as ReservaConsola
from gameheaven.models import ReservaVideojuego as ReservaVideojuego
from gameheaven.DAOs import daoUsuario as daoUsuario

### Daos reservas Consolas

def newReservaConsola(reservaConsola):
    reservaConsola.save()



def getReservasConsola():
    return ReservaConsola.objects.all()

def getReservaConsola(idReservaConsola):
    return ReservaConsola.objects.get(pk=idReservaConsola)

def getFechaReservaConsola(idReservaConsola):
    return getReservaConsola(idReservaConsola).fechaReserva

def getEstadoReservaConsola(idReservaConsola):
    return getReservaConsola(idReservaConsola).estado

def getStockConsolaReservaConsola(idReservaConsola):
    return getReservaConsola(idReservaConsola).stockConsola

def getClienteReservaConsola(idReservaConsola):
    return getReservaConsola(idReservaConsola).cliente



def filterReservasConsolaByCliente(idCliente):
    return ReservaConsola.objects.filter(cliente__id=idCliente)

def filterReservasConsolaByTienda(idTienda):
    return ReservaConsola.objects.filter(stockConsola__tienda__id=idTienda)

def filterReservasConsolaByConsola(idConsola):
    return ReservaConsola.objects.filter(stockConsola__consola__id=idConsola)

def filterReservasConsolaByEstado(estado):
    return ReservaConsola.objects.filter(estado=estado)

def filerReservasConsolaByFecha(fecha):
    return ReservaConsola.objects.filter(fecha=fecha)



def updateReservaConsola(idReserva, newReserva):
    reserva = getReservaConsola(idReserva)
    reserva.cliente = newReserva.cliente
    reserva.stockConsola = newReserva.stockConsola
    reserva.fecha = newReserva.fecha
    reserva.estado = newReserva.estado
    reserva.save()


def updateClienteReservaConsola(idReserva, cliente):
    reserva = getReservaConsola(idReserva)
    reserva.cliente = cliente
    reserva.save()

def updateStockConsolaReservaConsola(idReserva, stockConsola):
    reserva = getReservaConsola(idReserva)
    reserva.stockConsola = stockConsola
    reserva.save()

def updateReservasConsolaConsola(idReserva,idConsola):
    reserva = getReservaConsola(idReserva)
    reserva.consolaTienda__consola_id = idConsola
    reserva.save()

def updateReservasConsolaFecha(idReserva,fecha):
    reserva = getReservaConsola(idReserva)
    reserva.fecha = fecha
    reserva.save()

def updateReservasConsolaEstado(idReserva,estado):
    reserva = getReservaConsola(idReserva)
    reserva.estado = estado
    reserva.save()



def deleteReservaConsola(idReserva):
    reserva = getReservaConsola(idReserva)
    reserva.delete()





### Daos reservas Videojuegos

def newReservaVideojuego(reservaVideojuego):
    reservaVideojuego.save()



def getReservasVideojuego():
    return ReservaVideojuego.objects.all()

def getReservaVideojuego(idReservaVideojuego):
    return ReservaVideojuego.objects.get(pk=idReservaVideojuego)

def getClienteRservaVideojuego(idReservaVideojuego):
    return getReservaVideojuego(idReservaVideojuego).cliente

def getStockVideojuegoReservaVideojuego(idReservaVideojuego):
    return getReservaVideojuego(idReservaVideojuego).stockVideojuego

def getFechaReservaVideojuego(idReservaVideojuego):
    return getReservaVideojuego(idReservaVideojuego).fechaReserva

def getEstadoReservaVideojuego(idReservaVideojuego):
    return getReservaVideojuego(idReservaVideojuego).estado



def filterReservasVideojuegoByCliente(idCliente):
    return ReservaVideojuego.objects.filter(cliente_id=idCliente)
    
def filterReservasVideojuegoByTienda(idTienda):
    return ReservaVideojuego.objects.filter(stockVideojuego__tienda__id=idTienda)

def filterReservasVideojuegoByEstado(estado):
    return ReservaVideojuego.objects.filter(estado=estado)

def filterReservasVideojuegoByFecha(fecha):
    return ReservaVideojuego.objects.filter(fecha=fecha)



def updateReservaVideojuego(idReserva, NewReserva):
    reserva = getReservaVideojuego(idReserva)
    reserva.cliente = NewReserva.cliente
    reserva.stockVideojuego = NewReserva.stockVideojuego
    reserva.fecha = NewReserva.fecha
    reserva.estado = NewReserva.estado
    reserva.save()
    
def updateClienteReservaVideojuego(idReserva, cliente):
    reserva = getReservaVideojuego(idReserva)
    reserva.cliente = cliente
    reserva.save()

def updateStockVideojuegoReservaVideojuego(idReserva, stockVideojuego):
    reserva = getReservaVideojuego(idReserva)
    reserva.stockVideojuego = stockVideojuego
    reserva.save()

def updateFechaReservaVideojuego(idReserva, fecha):
    reserva = getReservaVideojuego(idReserva)
    reserva.fecha = fecha
    reserva.save()

def updateEstadoReservaVideojuego(idReserva, estado):
    reserva = getReservaVideojuego(idReserva)
    reserva.estado = estado
    reserva.save()


    
def deleteReservasVideojuego(idReserva):
    reserva = getReservaVideojuego(idReserva)
    reserva.delete()