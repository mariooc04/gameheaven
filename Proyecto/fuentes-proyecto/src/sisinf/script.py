""" from gameheaven.Constantes import ConstantesVOs as Constantes
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
 """

from steam import Steam
from decouple import config

urlGETListSteamAPI = "http://api.steampowered.com/ISteamApps/GetAppList/v2"

from steam import Steam
from decouple import config

KEY = config("STEAM_API_KEY")


steam = Steam(KEY)

#arguments: search
#user = steam.apps.search_games("ark")





user = steam.apps.get_app_details(346110, filters="metacritic")

# Guardo el resultado en formato json
import json
with open('data.json', 'w') as outfile:
    json.dump(user, outfile)

#juego = user['730']

print(user)