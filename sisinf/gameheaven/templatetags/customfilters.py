from django import template
from gameheaven.DAOs import daoProductos
import gameheaven.models as models

register = template.Library()

@register.filter(name='is_videojuego')
def is_videojuego(nombre):
    obj = daoProductos.getVideojuegoByNombre(nombre)
    return isinstance(obj, models.Videojuego)
