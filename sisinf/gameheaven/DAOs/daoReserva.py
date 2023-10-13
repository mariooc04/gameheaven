from gameheaven.models import ReservaConsola as ReservaConsola
from gameheaven.models import ReservaVideojuego as ReservaVideojuego

###Reservas Consolas

def newReservaConsola(reservaConsola):
    ReservaConsola.save(reservaConsola)

def newReservaVideojuego(reservaVideojuego):
    ReservaVideojuego.save(reservaVideojuego)
    
def getReservasConsola():
    return ReservaConsola.objects.all()

def  getReservasVideojuego():
    return ReservaVideojuego.objects.all()
    
def getReservasConsolaUsuario(idUsuario):
    return ReservaConsola.objects.filter(idUsuario=idUsuario)

def getReservaConsola(idReservaConsola):
    return ReservaConsola.objects.get(pk=idReservaConsola)

def getFechaReservaConsola(idReservaConsola):
    return ReservaConsola.objects.get(pk=idReservaConsola).fechaReserva

def getEstadoReservaConsola(idReservaConsola):
    return ReservaConsola.objects.get(pk=idReservaConsola).estado

def getConsolaReservaConsola(idReservaConsola):
    return ReservaConsola.objects.get(pk=idReservaConsola).idConsola

def getClienteReservaConsola(idReservaConsola):
    return ReservaConsola.objects.get(pk=idReservaConsola).idUsuario

def getReservasConsolaTienda(idTienda):
    return ReservaConsola.objects.filter(idTienda=idTienda)

def getReservasConsolaEstado(estado):
    return ReservaConsola.objects.filter(estado=estado)

def getReservasConsolaFecha(fecha):
    return ReservaConsola.objects.filter(fecha=fecha)

def getReservasConsolaFechaEstado(fecha, estado):
    return ReservaConsola.objects.filter(fecha=fecha, estado=estado)

def getReservasConsolaTiendaEstado(idTienda, estado):
    return ReservaConsola.objects.filter(idTienda=idTienda, estado=estado)
    
def getReservasConsolaTiendaFecha(idTienda, fecha):
    return ReservaConsola.objects.filter(idTienda=idTienda, fecha=fecha)

def getReservasConsolaTiendaFechaEstado(idTienda, fecha, estado):
    return ReservaConsola.objects.filter(idTienda=idTienda, fecha=fecha, estado=estado)

def getReservasConsolaUsuarioEstado(idUsuario, estado):
    return ReservaConsola.objects.filter(idUsuario=idUsuario, estado=estado)

def getReservasConsolaUsuarioFecha(idUsuario, fecha):
    return ReservaConsola.objects.filter(idUsuario=idUsuario, fecha=fecha)

def updateReservasConsola(idReserva, NewReserva):
    reserva = getReservaConsola(idReserva)
    reserva.idUsuario = NewReserva.idUsuario
    reserva.idTienda = NewReserva.idTienda
    reserva.idConsola = NewReserva.idConsola
    reserva.fecha = NewReserva.fecha
    reserva.estado = NewReserva.estado
    reserva.save()



def updateUsuarioReservasConsola(idReserva,idUsuario):
    reserva = getReservaConsola(idReserva)
    reserva.idUsuario = idUsuario
    reserva.save()

def updateTiendaReservasConsola(idReserva,idTienda):
    reserva = getReservaConsola(idReserva)
    reserva.idTienda = idTienda
    reserva.save()

def updateConsolaReservasConsola(idReserva,idConsola):
    reserva = getReservaConsola(idReserva)
    reserva.idConsola = idConsola
    reserva.save()

def updateFechaReservasConsola(idReserva,fecha):
    reserva = getReservaConsola(idReserva)
    reserva.fecha = fecha
    reserva.save()

def updateEstadoReservasConsola(idReserva,estado):
    reserva = getReservaConsola(idReserva)
    reserva.estado = estado
    reserva.save()

def deleteReservasConsola(idReserva):
    reserva = getReservaConsola(idReserva)
    reserva.delete()

    
### ReservasVidejuegos

def newReservaVideojuego(reservaVideojuego):
    ReservaVideojuego.save(reservaVideojuego)

def getReservasVideojuego():
    return ReservaVideojuego.objects.all()

def getReservasVideojuegoUsuario(idUsuario):
    return ReservaVideojuego.objects.filter(idUsuario=idUsuario)

def getReservaVideojuego(idReservaVideojuego):
    return ReservaVideojuego.objects.get(pk=idReservaVideojuego)

def getReservasVideojuegoTienda(idTienda):
    return ReservaVideojuego.objects.filter(idTienda=idTienda)

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

def getReservasVideojuegoFechaEstado(fecha, estado):
    return ReservaVideojuego.objects.filter(fecha=fecha, estado=estado)

def getReservasVideojuegoTiendaEstado(idTienda, estado):
    return ReservaVideojuego.objects.filter(idTienda=idTienda, estado=estado)

def getReservasVideojuegoTiendaFecha(idTienda, fecha):
    return ReservaVideojuego.objects.filter(idTienda=idTienda, fecha=fecha)

def getReservasVideojuegoTiendaFechaEstado(idTienda, fecha, estado):
    return ReservaVideojuego.objects.filter(idTienda=idTienda, fecha=fecha, estado=estado)

def getReservasVideojuegoUsuarioEstado(idUsuario, estado):
    return ReservaVideojuego.objects.filter(idUsuario=idUsuario, estado=estado)

def getReservasVideojuegoUsuarioFecha(idUsuario, fecha):
    return ReservaVideojuego.objects.filter(idUsuario=idUsuario, fecha=fecha)

def updateReservasVideojuego(idReserva, NewReserva):
    reserva = getReservaVideojuego(idReserva)
    reserva.idUsuario = NewReserva.idUsuario
    reserva.idTienda = NewReserva.idTienda
    reserva.idVideojuego = NewReserva.idVideojuego
    reserva.fecha = NewReserva.fecha
    reserva.estado = NewReserva.estado
    reserva.save()
    
def updateidUsuarioReservaVideojuego(idReserva, idUsuario):
    reserva = getReservaVideojuego(idReserva)
    reserva.idUsuario = idUsuario
    reserva.save()
    
def updateidTiendaReservaVideojuego(idReserva, idTienda):
    reserva = getReservaVideojuego(idReserva)
    reserva.idTienda = idTienda
    reserva.save()

def updateidVideojuegoReservaVideojuego(idReserva, idVideojuego):
    reserva = getReservaVideojuego(idReserva)
    reserva.idVideojuego = idVideojuego
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