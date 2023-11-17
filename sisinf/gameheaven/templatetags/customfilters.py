from django import template
from gameheaven.DAOs import daoProductos,daoTienda
import gameheaven.models as models

register = template.Library()

@register.filter(name='is_videojuego')
def is_videojuego(nombre):
    try:
        obj = daoProductos.getVideojuegoByNombre(nombre)
    except:
        return False
    return isinstance(obj, models.Videojuego)

@register.filter(name='getPrecio')
def getPrecio(producto,Tienda):
    if(isinstance(producto, models.Videojuego)):
        precio = daoTienda.getPrecioStockVideojuego(Tienda, producto)
        return precio
    elif(isinstance(producto, models.Consola)):
        precio = daoTienda.getPrecioStockConsola(Tienda, producto)
        return precio


    
    
