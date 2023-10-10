from django.db import models

ESTADOS = {
    ('estadoNoCompletada', 'No completada'),
    ('estadoCompletada', 'Completada')
}

# Create your models here.
class Tienda(models.Model):
    ciudad = models.CharField(max_length=50)
    codigoPostal = models.IntegerField()


    

class Videojuego(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=500, null=True)
    valoracion = models.FloatField(null=True)
    plataformas = models.CharField(max_length=50, null=True)
    img = models.ImageField(upload_to='img/', null=True)
    
    
class Consola(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=500, null=True)
    img = models.ImageField(upload_to='img/', null=True)
    valoracion = models.FloatField(null=True)

class StockVideojuego(models.Model):
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)
    videojuego = models.ForeignKey(Videojuego, on_delete=models.CASCADE)
    precio = models.FloatField()
    stock = models.IntegerField()

class StockConsolas(models.Model):
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)
    consola = models.ForeignKey(Consola, on_delete=models.CASCADE)
    precio = models.FloatField()
    stock = models.IntegerField()

class Administrador(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    usuario = models.CharField(max_length=50)

class Cliente(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    usuario = models.CharField(max_length=50)
    idTienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)
    


class Trabajador(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    usuario = models.CharField(max_length=50)
    idTienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)
    idAdmin = models.ForeignKey(Administrador, on_delete=models.CASCADE)

class ReservaVideojuego(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    videojuegoTienda = models.ForeignKey(StockVideojuego, on_delete=models.CASCADE)
    fecha = models.DateField()
    estado = models.CharField(max_length=50, choices=ESTADOS)

class ReservaConsola(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    consolaTienda = models.ForeignKey(StockConsolas, on_delete=models.CASCADE)
    fecha = models.DateField()
    estado = models.CharField(max_length=50, choices=ESTADOS)