from gameheaven.models import Trabajador as Trabajador
from gameheaven.models import TrabajadorProfile as TrabajadorProfile
from gameheaven.models import Cliente as Cliente
from gameheaven.models import CustomUser as CustomUser
from gameheaven.DAOs import daoTienda as daoTienda


### Daos Usuario
def existeUsuario(email):
    return Trabajador.objects.filter(email=email).exists() or Cliente.objects.filter(email=email).exists()
### Daos Trabajador

def newTrabajador(email, name, password, tienda):
    trabajador = Trabajador(email=email, name=name, password=password)
    trabajador.save()
    TrabajadorProfile.objects.create(user=trabajador, tienda=tienda)
    

    
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

def filterTrabajadorByEmail(email):
    return Trabajador.objects.filter(email=email)

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

#DELETES

def deleteTrabajador(trabajador):
    if isinstance(trabajador, int):
        trabajador = getTrabajador(trabajador)
    trabajador.delete()


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

def checkPasswordCliente(cliente, password):
    return getCliente(cliente).password == password

def filterClienteByEmail(email):
    return Cliente.objects.filter(email=email)

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
