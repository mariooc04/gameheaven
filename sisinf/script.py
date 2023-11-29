from gameheaven.Constantes import ConstantesVOs as Constantes
from django.contrib.auth.models import Group, Permission

# Create groups
groupTrabajadores, created = Group.objects.get_or_create(name=Constantes.GRUPO_TRABAJADORES)
groupClientes, created = Group.objects.get_or_create(name=Constantes.GRUPO_CLIENTES)


# Set permissions for groupTrabajadores
permisosTrabajador = Permission.objects.filter(codename__in=Constantes.getPermisosTrabajador())
groupTrabajadores.permissions.set(permisosTrabajador)

# Set permissions for groupClientes
permisosCliente = Permission.objects.filter(codename__in=Constantes.getPermisosCliente())
groupClientes.permissions.set(permisosCliente)