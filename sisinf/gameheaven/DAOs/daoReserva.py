from gameheaven.models import ReservaConsola as ReservaConsola
from gameheaven.models import ReservaVideojuego as ReservaVideojuego
from gameheaven.DAOs import daoUsuario as daoUsuario

### Daos reservas Consolas

def newReservaConsola(reservaConsola):
    reservaConsola.save()

#GETTERS (with ID)

def getAllReservasConsola():
    return ReservaConsola.objects.all()

def getReservaConsola(idReserva):
    return ReservaConsola.objects.get(pk=idReserva)

def getFechaReservaConsola(idReserva):
    return getReservaConsola(idReserva).fecha

def getEstadoReservaConsola(idReserva):
    return getReservaConsola(idReserva).estado

def getStockConsolaReservaConsola(idReserva):
    return getReservaConsola(idReserva).stockConsola

def getClienteReservaConsola(idReserva):
    return getReservaConsola(idReserva).cliente

#FILTERS (with ID and Object)

def filterReservasConsolaByCliente(cliente):
    return ReservaConsola.objects.filter(cliente=cliente)

def filterReservasConsolaByTienda(tienda):
    return ReservaConsola.objects.filter(stockConsola__tienda=tienda)

def filterReservasConsolaByConsola(consola):
    return ReservaConsola.objects.filter(stockConsola__consola=consola)

def filterReservasConsolaByEstado(estado):
    return ReservaConsola.objects.filter(estado=estado)

def filerReservasConsolaByFecha(fecha):
    return ReservaConsola.objects.filter(fecha=fecha)

#UPDATES

def updateReservaConsola(reserva, newReserva):
    if isinstance(reserva, int):
        reserva = getReservaConsola(reserva)
    reserva.cliente = newReserva.cliente
    reserva.stockConsola = newReserva.stockConsola
    reserva.fecha = newReserva.fecha
    reserva.estado = newReserva.estado
    reserva.save()


def updateClienteReservaConsola(reserva, cliente):
    if isinstance(reserva, int):
        reserva = getReservaConsola(reserva)
    reserva.cliente = cliente
    reserva.save()

def updateStockConsolaReservaConsola(reserva, stockConsola):
    if isinstance(reserva, int):
        reserva = getReservaConsola(reserva)
    reserva.stockConsola = stockConsola
    reserva.save()

def updateReservasConsolaConsola(reserva,idConsola):
    if isinstance(reserva, int):
        reserva = getReservaConsola(reserva)
    reserva.consolaTienda__consola_id = idConsola
    reserva.save()

def updateReservasConsolaFecha(reserva,fecha):
    if isinstance(reserva, int):
        reserva = getReservaConsola(reserva)
    reserva.fecha = fecha
    reserva.save()

def updateReservasConsolaEstado(reserva,estado):
    if isinstance(reserva, ReservaConsola):
        reserva = reserva.id
    reserva.estado = estado
    reserva.save()

#DELETES

def deleteReservaConsola(reserva):
    if isinstance(reserva, int):
        reserva = getReservaConsola(reserva)
    reserva.delete()

### Daos reservas Videojuegos

def newReservaVideojuego(reservaVideojuego):
    reservaVideojuego.save()

#GETTERS (with ID)

def getAllReservasVideojuego():
    return ReservaVideojuego.objects.all()

def getReservaVideojuego(idReserva):
    return ReservaVideojuego.objects.get(pk=idReserva)

def getClienteRservaVideojuego(idReserva):
    return getReservaVideojuego(idReserva).cliente

def getStockVideojuegoReservaVideojuego(idReserva):
    return getReservaVideojuego(idReserva).stockVideojuego

def getFechaReservaVideojuego(idReserva):
    return getReservaVideojuego(idReserva).fecha

def getEstadoReservaVideojuego(idReserva):
    return getReservaVideojuego(idReserva).estado

#FILTERS (with ID and Object)

def filterReservasVideojuegoByCliente(cliente):
    return ReservaVideojuego.objects.filter(cliente=cliente)
    
def filterReservasVideojuegoByTienda(tienda):
    return ReservaVideojuego.objects.filter(stockVideojuego__tienda=tienda)

def filterReservasVideojuegoByEstado(estado):
    return ReservaVideojuego.objects.filter(estado=estado)

def filterReservasVideojuegoByFecha(fecha):
    return ReservaVideojuego.objects.filter(fecha=fecha)

#UPDATES

def updateReservaVideojuego(reserva, NewReserva):
    if isinstance(reserva, int):
        reserva = getReservaVideojuego(reserva)
    reserva.cliente = NewReserva.cliente
    reserva.stockVideojuego = NewReserva.stockVideojuego
    reserva.fecha = NewReserva.fecha
    reserva.estado = NewReserva.estado
    reserva.save()
    
def updateClienteReservaVideojuego(reserva, cliente):
    if isinstance(reserva, int):
        reserva = getReservaVideojuego(reserva)
    reserva.cliente = cliente
    reserva.save()

def updateStockVideojuegoReservaVideojuego(reserva, stockVideojuego):
    if isinstance(reserva, int):
        reserva = getReservaVideojuego(reserva)
    reserva.stockVideojuego = stockVideojuego
    reserva.save()

def updateFechaReservaVideojuego(reserva, fecha):
    if isinstance(reserva, int):
        reserva = getReservaVideojuego(reserva)
    reserva.fecha = fecha
    reserva.save()

def updateEstadoReservaVideojuego(reserva, estado):
    if isinstance(reserva, int):
        reserva = getReservaVideojuego(reserva)
    reserva.estado = estado
    reserva.save()

#DELETES
    
def deleteReservasVideojuego(reserva):
    if isinstance(reserva, int):
        reserva = getReservaVideojuego(reserva)
    reserva.delete()