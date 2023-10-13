from models import Trabajador as Trabajador
from models import Administrador as Administrador
from models import Cliente as Cliente

###Trabajadores

def checkPasswordTrabajador(idTrabajador, password):
    return getTrabajador(idTrabajador).password == password

def newTrajador(trabajador):
    Trabajador.save(trabajador)

def getTrabajador(idTrabajador):
    return Trabajador.objects.get(pk=idTrabajador)

def getEmailTrabajador(idTrabajador):
    return getTrabajador(idTrabajador).email

def getUsuarioTrabajador(idTrabajador):
    return getTrabajador(idTrabajador).usuario

def getIdTiendaTrabajador(idTrabajador):
    return getTrabajador(idTrabajador).idTienda

def getIdAdminTrabajador(idTrabajador):
    return getTrabajador(idTrabajador).idAdmin

def getTrabajadoresTienda(idTienda):
    return Trabajador.objects.filter(tienda=idTienda)

def getTrabajadoresAdmin(idAdmin):
    return Trabajador.objects.filter(idAdmin=idAdmin)

def updateTrabajador(idTrabajador, newTrabajador):
    trabajador = getTrabajador(idTrabajador)
    trabajador.email = newTrabajador.email
    trabajador.password = newTrabajador.password
    trabajador.usuario = newTrabajador.usuario
    trabajador.idTienda = newTrabajador.idTienda
    trabajador.idAdmin = newTrabajador.idAdmin
    trabajador.save()

def updateEmailTrabajador(idTrabajador, email):
    trabajador = getTrabajador(idTrabajador)
    trabajador.email = email
    trabajador.save()

def updatePasswordTrabajador(idTrabajador, password):
    trabajador = getTrabajador(idTrabajador)
    trabajador.password = password
    trabajador.save()

def updateUsuarioTrabajador(idTrabajador, usuario):
    trabajador = getTrabajador(idTrabajador)
    trabajador.usuario = usuario
    trabajador.save()

def updateIdTiendaTrabajador(idTrabajador, idTienda):
    trabajador = getTrabajador(idTrabajador)
    trabajador.idTienda = idTienda
    trabajador.save()

def updateIdAdminTrabajador(idTrabajador, idAdmin):
    trabajador = getTrabajador(idTrabajador)
    trabajador.idAdmin = idAdmin
    trabajador.save()

def deleteTrabajador(idTrabajador):
    Trabajador.objects.get(pk=idTrabajador).delete()

###Administradores

def checkPasswordAdministrador(idAdministrador, password):
    return getAdministrador(idAdministrador).password == password

def newAdministrador(administrador):
    Administrador.save(administrador)

def getAdministrador(idAdministrador):
    return Administrador.objects.get(pk=idAdministrador)

def getEmailAdministrador(idAdministrador):
    return getAdministrador(idAdministrador).email

def getUsuarioAdministrador(idAdministrador):
    return getAdministrador(idAdministrador).usuario

def getAdministradores():
    return Administrador.objects.all()

def updateAdministrador(idAdministrador, newAdministrador):
    administrador = getAdministrador(idAdministrador)
    administrador.email = newAdministrador.email
    administrador.password = newAdministrador.password
    administrador.usuario = newAdministrador.usuario
    administrador.save()

def updateEmailAdministrador(idAdministrador, email):
    administrador = getAdministrador(idAdministrador)
    administrador.email = email
    administrador.save()

def updatePasswordAdministrador(idAdministrador, password):
    administrador = getAdministrador(idAdministrador)
    administrador.password = password
    administrador.save()

def updateUsuarioAdministrador(idAdministrador, usuario):
    administrador = getAdministrador(idAdministrador)
    administrador.usuario = usuario
    administrador.save()

def deleteAdministrador(idAdministrador):
    Administrador.objects.get(pk=idAdministrador).delete()

###Clientes

def checkPasswordCliente(idCliente, password):
    return getCliente(idCliente).password == password

def newCliente(cliente):
    Cliente.save(cliente)

def getCliente(idCliente):
    return Cliente.objects.get(pk=idCliente)

def getEmailCliente(idCliente):
    return getCliente(idCliente).email

def getUsuarioCliente(idCliente):
    return getCliente(idCliente).usuario

def getIdTiendaCliente(idCliente):
    return getCliente(idCliente).idTienda

def getClientesTienda(idTienda):
    return Cliente.objects.filter(idTienda=idTienda)

def updateCliente(idCliente, newCliente):
    cliente = getCliente(idCliente)
    cliente.email = newCliente.email
    cliente.password = newCliente.password
    cliente.usuario = newCliente.usuario
    cliente.idTienda = newCliente.idTienda
    cliente.save()

def updateEmailCliente(idCliente, email):
    cliente = getCliente(idCliente)
    cliente.email = email
    cliente.save()

def updatePasswordCliente(idCliente, password):
    cliente = getCliente(idCliente)
    cliente.password = password
    cliente.save()

def updateUsuarioCliente(idCliente, usuario):
    cliente = getCliente(idCliente)
    cliente.usuario = usuario
    cliente.save()

def updateIdTiendaCliente(idCliente, idTienda):
    cliente = getCliente(idCliente)
    cliente.idTienda = idTienda
    cliente.save()

def deleteCliente(idCliente):
    Cliente.objects.get(pk=idCliente).delete()