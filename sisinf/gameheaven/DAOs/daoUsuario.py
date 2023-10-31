from gameheaven.models import Usuario, Trabajador, Cliente
from gameheaven.DAOs import daoTienda


### Daos Usuario
def existeUsuarioEmail(email):
    return Usuario.objects.filter(email=email).exists()

def existeUsuarioUsername(username):
    return Usuario.objects.filter(username=username).exists()

def getUsuario(idUsuario):
    return Usuario.objects.get(pk=idUsuario)

def getUsuarioByEmail(email):
    return Usuario.objects.get(email=email)

def getEmailUsuario(idUsuario):
    return getUsuario(idUsuario).email


def getUsernameUsuario(idUsuario):
    return getUsuario(idUsuario).username

def deleteUser(usuario):
    if isinstance(usuario, int):
        usuario = getUsuario(usuario)
    usuario.delete()
def deleteTrabajador(email):
    trabajador = getUsuarioByEmail(email)
    trabajador.delete()

### Daos Trabajador
def newTrabajador(email, password, username):
    return Usuario.objects.create_user(email=email, password=password, username=username, role=Usuario.Roles.TRABAJADOR)

def getTrabajadorByUsuario(usuario):
    return Trabajador.objects.get(usuario=usuario)

def getAllTrabajadores():
    return Trabajador.objects.all()

def updateTiendaTrabajador(usuario, tienda):
    if isinstance(usuario, int):
        usuario = getUsuario(usuario)
    if isinstance(tienda, int):
        tienda = daoTienda.getTienda(tienda)
    trabajador = getTrabajadorByUsuario(usuario)
    trabajador.tienda = tienda
    trabajador.save()

### Daos Cliente
def newCliente(usuario):
    return Usuario.objects.create_user(email=usuario.email, password=usuario.password, 
                                       username=usuario.username, role=Usuario.Roles.CLIENTE)

def getClienteByUsuario(usuario):
    return Cliente.objects.get(usuario=usuario)


def updateTiendaCliente(usuario, tienda):
    if isinstance(tienda, int):
        tienda = daoTienda.getTienda(tienda)
    cliente = getClienteByUsuario(usuario)
    cliente.tienda = tienda
    cliente.save()

