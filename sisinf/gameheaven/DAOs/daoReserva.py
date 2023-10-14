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

def getConsolaReservaConsola(idReservaConsola):
    return getReservaConsola(idReservaConsola).consolaTienda__consola_id   

def getClienteReservaConsola(idReservaConsola):
    return getReservaConsola(idReservaConsola).cliente_id

def filterReservasConsolaByCliente(idCliente):
    return ReservaConsola.objects.filter(cliente_id=idCliente)

def filterReservasConsolaByTienda(idTienda):
    return ReservaConsola.objects.filter(consolaTienda__tienda_id=idTienda)

def filterReservasConsolaByEstado(estado):
    return ReservaConsola.objects.filter(estado=estado)

def filerReservasConsolaByFecha(fecha):
    return ReservaConsola.objects.filter(fecha=fecha)

def updateReservasConsola(idReserva, NewReserva):
    reserva = getReservaConsola(idReserva)
    reserva.cliente_id = NewReserva.cliente
    reserva.consolaTienda = NewReserva.consolaTienda
    reserva.fecha = NewReserva.fecha
    reserva.estado = NewReserva.estado
    reserva.save()


def updateReservasConsolaCliente(idReserva, idCliente):
    reserva = getReservaConsola(idReserva)
    reserva.cliente_id = idCliente
    reserva.save()

def updateReservasConsolaTienda(idReserva,idTienda):
    reserva = getReservaConsola(idReserva)
    reserva.consolaTienda__tienda_id = idTienda
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

def  getReservasVideojuego():
    return ReservaVideojuego.objects.all()

def getReservaVideojuego(idReservaVideojuego):
    return ReservaVideojuego.objects.get(pk=idReservaVideojuego)

def getReservasVideojuegoCliente(idCliente):
    return ReservaVideojuego.objects.filter(cliente_id=idCliente)
    
def getReservasVideojuegoTienda(idTienda):
    return ReservaVideojuego.objects.filter(videojuegoTienda__tienda_id=idTienda)

def getFechaReservaVideojuego(idReservaVideojuego):
    return getReservaVideojuego(idReservaVideojuego).fechaReserva

def getEstadoReservaVideojuego(idReservaVideojuego):
    return getReservaVideojuego(idReservaVideojuego).estado

def getVideojuegoReservaVideojuego(idReservaVideojuego):
    return getReservaVideojuego(idReservaVideojuego).idVideojuego

def getReservasVideojuegoEstado(estado):
    return ReservaVideojuego.objects.filter(estado=estado)

def getReservasVideojuegoFecha(fecha):
    return ReservaVideojuego.objects.filter(fecha=fecha)

def updateReservasVideojuego(idReserva, NewReserva):
    reserva = getReservaVideojuego(idReserva)
    reserva.cliente_id = NewReserva.cliente
    reserva.videojuegoTienda = NewReserva.videojuegoTienda
    reserva.fecha = NewReserva.fecha
    reserva.estado = NewReserva.estado
    reserva.save()
    
def updateReservasVideojuegoTienda(idReserva, idTienda):
    reserva = getReservaVideojuego(idReserva)
    reserva.videojuegoTienda__tienda_id = idTienda
    reserva.save()

def updateidVideojuegoReservaVideojuego(idReserva, idVideojuego):
    reserva = getReservaVideojuego(idReserva)
    reserva.videojuegoTienda__videojuego_id = idVideojuego
    reserva.save()

def updateReservasVideojuegoCliente(idReserva, idCliente):
    reserva = getReservaVideojuego(idReserva)
    reserva.cliente_id = idCliente
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