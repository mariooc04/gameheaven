from gameheaven.models import CustomUser, Trabajador, Cliente
from gameheaven.DAOs import daoTienda


### Daos Usuario
def existeUsuario(email):
    return CustomUser.objects.filter(email=email).exists()

def getUsuario(idUsuario):
    return CustomUser.objects.get(pk=idUsuario)

def getEmailUsuario(idUsuario):
    return getUsuario(idUsuario).email

def getUsernameUsuario(idUsuario):
    return getUsuario(idUsuario).username

def deleteUser(usuario):
    if isinstance(usuario, int):
        usuario = getUsuario(usuario)
    usuario.delete()

### Daos Trabajador
def newTrabajador(email, password, username):
    return CustomUser.objects.create_user(email=email, password=password, username=username, role=CustomUser.Roles.TRABAJADOR)

def getTrabajadorByUsuario(usuario):
    return Trabajador.objects.get(usuario=usuario)

def updateTiendaTrabajador(usuario, tienda):
    if isinstance(usuario, int):
        usuario = getUsuario(usuario)
    if isinstance(tienda, int):
        tienda = daoTienda.getTienda(tienda)
    trabajador = getTrabajadorByUsuario(usuario)
    trabajador.tienda = tienda
    trabajador.save()

### Daos Cliente
def newCliente(email, password, username):
    return CustomUser.objects.create_user(email=email, password=password, username=username, role=CustomUser.Roles.CLIENTE)

def getClienteByUsuario(usuario):
    return Cliente.objects.get(usuario=usuario)

def updateTiendaCliente(usuario, tienda):
    if isinstance(usuario, int):
        usuario = getUsuario(usuario)
    if isinstance(tienda, int):
        tienda = daoTienda.getTienda(tienda)
    cliente = getClienteByUsuario(usuario)
    cliente.tienda = tienda
    cliente.save()

