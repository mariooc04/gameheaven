from gameheaven.Constantes import ConstantesVOs as Constantes
from django.contrib.auth.models import Group, Permission
from gameheaven.models import Usuario as User

#Create superuser
if not User.objects.filter(email="gameheaven.adm@gmail.com").exists():
    User.objects.create_superuser("gameheaven.adm@gmail.com","gameheaven","gameheaven.administrator1234")

# Create groups
groupTrabajadores, createdTrabajadores = Group.objects.get_or_create(name=Constantes.GRUPO_TRABAJADORES)
groupClientes, createdClientes = Group.objects.get_or_create(name=Constantes.GRUPO_CLIENTES)


# Set permissions for groupTrabajadores
if createdTrabajadores:
    permisosTrabajador = Permission.objects.filter(codename__in=Constantes.getPermisosTrabajador())
    groupTrabajadores.permissions.set(permisosTrabajador)

# Set permissions for groupClientes
if createdClientes:
    permisosCliente = Permission.objects.filter(codename__in=Constantes.getPermisosCliente())
    groupClientes.permissions.set(permisosCliente)