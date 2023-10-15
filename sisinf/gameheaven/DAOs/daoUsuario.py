from gameheaven.models import Trabajador as Trabajador
from gameheaven.models import Administrador as Administrador
from gameheaven.models import Cliente as Cliente
from gameheaven.DAOs import daoTienda as daoTienda

### Daos Trabajador

def newTrajador(trabajador):
    Trabajador.save(trabajador)

#GETTERS (with ID)

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

#FILTERS (with ID)

def filterTrabajadoresByTienda(idTienda):
    return Trabajador.objects.filter(tienda_id=idTienda)

def filterTrabajadoresByAdmin(idAdmin):
    return Trabajador.objects.filter(administrador_id=idAdmin)

#UPDATES

def updateTrabajador(trabajador, newTrabajador):
    if isinstance(trabajador, int):
        trabajador = getTrabajador(trabajador)
    trabajador.email = newTrabajador.email
    trabajador.password = newTrabajador.password
    trabajador.usuario = newTrabajador.usuario
    trabajador.tienda = newTrabajador.tienda
    trabajador.administrador = newTrabajador.administrador
    trabajador.save()

def updateEmailTrabajador(trabajador, email):
    if isinstance(trabajador, int):
        trabajador = getTrabajador(trabajador)
    trabajador.email = email
    trabajador.save()

def updatePasswordTrabajador(trabajador, password):
    if isinstance(trabajador, int):
        trabajador = getTrabajador(trabajador)
    trabajador.password = password
    trabajador.save()

def updateUsuarioTrabajador(trabajador, usuario):
    if isinstance(trabajador, int):
        trabajador = getTrabajador(trabajador)
    trabajador.usuario = usuario
    trabajador.save()

def updateTiendaTrabajador(trabajador, tienda):
    if isinstance(trabajador, int):
        trabajador = getTrabajador(trabajador)
    if isinstance(tienda, int):
        tienda = daoTienda.getTienda(tienda)
    trabajador.tienda = tienda
    trabajador.save()

def updateAdministradorTrabajador(trabajador, administrador):
    if isinstance(trabajador, int):
        trabajador = getTrabajador(trabajador)
    if isinstance(administrador, int):
        administrador = getAdministrador(administrador)
    trabajador.administrador = administrador
    trabajador.save()

#DELETES

def deleteTrabajador(trabajador):
    if isinstance(trabajador, int):
        trabajador = getTrabajador(trabajador)
    trabajador.delete()



###Administradores

def newAdministrador(administrador):
    Administrador.save(administrador)

#GETTERS (with ID)

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

#UPDATES

def updateAdministrador(administrador, newAdministrador):
    if isinstance(administrador, int):
        administrador = getAdministrador(administrador)
    administrador.email = newAdministrador.email
    administrador.password = newAdministrador.password
    administrador.usuario = newAdministrador.usuario
    administrador.save()

def updateEmailAdministrador(administrador, email):
    if isinstance(administrador, int):
        administrador = getAdministrador(administrador)
    administrador.email = email
    administrador.save()

def updatePasswordAdministrador(administrador, password):
    if isinstance(administrador, int):
        administrador = getAdministrador(administrador)
    administrador.password = password
    administrador.save()

def updateUsuarioAdministrador(administrador, usuario):
    if isinstance(administrador, int):
        administrador = getAdministrador(administrador)
    administrador.usuario = usuario
    administrador.save()

#DELETES

def deleteAdministrador(administrador):
    if isinstance(administrador, int):
        administrador = getAdministrador(administrador)
    administrador.delete()


### Daos Cliente

def newCliente(cliente):
    Cliente.save(cliente)

#GETTERS (with ID)

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

#UPDATES

def updateCliente(cliente, newCliente):
    if isinstance(cliente, int):
        cliente = getCliente(cliente)
    cliente.email = newCliente.email
    cliente.password = newCliente.password
    cliente.usuario = newCliente.usuario
    cliente.tienda = newCliente.tienda
    cliente.save()

def updateEmailCliente(cliente, email):
    if isinstance(cliente, int):
        cliente = getCliente(cliente)
    cliente.email = email
    cliente.save()

def updatePasswordCliente(cliente, password):
    if isinstance(cliente, int):
        cliente = getCliente(cliente)
    cliente.password = password
    cliente.save()

def updateUsuarioCliente(cliente, usuario):
    if isinstance(cliente, int):
        cliente = getCliente(cliente)
    cliente.usuario = usuario
    cliente.save()

def updateTiendaCliente(cliente, tienda):
    if isinstance(cliente, int):
        cliente = getCliente(cliente)
    if isinstance(tienda, int):
        tienda = daoTienda.getTienda(tienda)
    cliente.tienda = tienda
    cliente.save()

#DELETES

def deleteCliente(cliente):
    if isinstance(cliente, int):
        cliente = getCliente(cliente)
    cliente.delete()