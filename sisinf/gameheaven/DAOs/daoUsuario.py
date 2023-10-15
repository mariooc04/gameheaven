from gameheaven.models import Trabajador as Trabajador
from gameheaven.models import Administrador as Administrador
from gameheaven.models import Cliente as Cliente
from gameheaven.DAOs import daoTienda as daoTienda

### Daos Trabajador

def newTrajador(trabajador):
    Trabajador.save(trabajador)



def getAllTrabajadores():
    return Trabajador.objects.all()

def getTrabajador(idTrabajador):
    return Trabajador.objects.get(pk=idTrabajador)

def getEmailTrabajador(idTrabajador):
    return getTrabajador(idTrabajador).email

def getUsuarioTrabajador(idTrabajador):
    return getTrabajador(idTrabajador).usuario

def getTiendaTrabajador(idTrabajador):
    return getTrabajador(idTrabajador).tienda

def getAdministradorTrabajador(idTrabajador):
    return getTrabajador(idTrabajador).administrador 

def checkPasswordTrabajador(idTrabajador, password):
    return getTrabajador(idTrabajador).password == password



def filterTrabajadoresByTienda(idTienda):
    return Trabajador.objects.filter(tienda_id=idTienda)

def filterTrabajadoresByAdmin(idAdmin):
    return Trabajador.objects.filter(administrador_id=idAdmin)



def updateTrabajador(idTrabajador, newTrabajador):
    trabajador = getTrabajador(idTrabajador)
    trabajador.email = newTrabajador.email
    trabajador.password = newTrabajador.password
    trabajador.usuario = newTrabajador.usuario
    trabajador.tienda = newTrabajador.tienda
    trabajador.administrador = newTrabajador.administrador
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

def updateTiendaTrabajador(idTrabajador, idTienda):
    trabajador = getTrabajador(idTrabajador)
    tienda = daoTienda.getTienda(idTienda)
    trabajador.tienda = tienda
    trabajador.save()

def updateAdministradorTrabajador(idTrabajador, idAdmin):
    trabajador = getTrabajador(idTrabajador)
    administrador = getAdministrador(idAdmin)
    trabajador.administrador = administrador
    trabajador.save()



def deleteTrabajador(idTrabajador):
    getTrabajador(idTrabajador).delete()



###Administradores

def newAdministrador(administrador):
    Administrador.save(administrador)



def getAllAdministradores():
    return Administrador.objects.all()

def getAdministrador(idAdministrador):
    return Administrador.objects.get(pk=idAdministrador)

def getEmailAdministrador(idAdministrador):
    return getAdministrador(idAdministrador).email

def getUsuarioAdministrador(idAdministrador):
    return getAdministrador(idAdministrador).usuario

def checkPasswordAdministrador(idAdministrador, password):
    return getAdministrador(idAdministrador).password == password



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



def deleteAdministrador(administrador):
    Administrador.objects.get(pk=administrador.id).delete()

### Daos Cliente

def newCliente(cliente):
    Cliente.save(cliente)



def getAllClientes():
    return Cliente.objects.all()

def getCliente(idCliente):
    return Cliente.objects.get(pk=idCliente)

def getEmailCliente(idCliente):
    return getCliente(idCliente).email

def getUsuarioCliente(idCliente):
    return getCliente(idCliente).usuario

def getTiendaCliente(idCliente):
    return getCliente(idCliente).tienda

def checkPasswordCliente(idCliente, password):
    return getCliente(idCliente).password == password



def updateCliente(idCliente, newCliente):
    cliente = getCliente(idCliente)
    cliente.email = newCliente.email
    cliente.password = newCliente.password
    cliente.usuario = newCliente.usuario
    cliente.tienda = newCliente.tienda
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

def updateTiendaCliente(idCliente, idTienda):
    cliente = getCliente(idCliente)
    tienda = daoTienda.getTienda(idTienda)
    cliente.tienda = tienda
    cliente.save()



def deleteCliente(cliente):
    Cliente.objects.get(pk=cliente.id).delete()