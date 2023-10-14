from django.db import models

# Create your models here.
class Tienda(models.Model):
    ciudad = models.CharField(max_length=50)
    codigoPostal = models.IntegerField()
    videojuegos = models.ManyToManyField('Videojuego', through='StockVideojuego')
    consolas = models.ManyToManyField('Consola', through='StockConsolas')
    

class Videojuego(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=500, null=True)
    valoracion = models.FloatField(null=True)
    plataformas = models.CharField(max_length=50, null=True)
    img = models.ImageField(upload_to='img/', null=True)
    
    
class Consola(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=500, null=True)
    valoracion = models.FloatField(null=True)
    img = models.ImageField(upload_to='img/', null=True)
    

class StockVideojuego(models.Model):
    tienda_id = models.ForeignKey(Tienda, on_delete=models.CASCADE)
    videojuego_id = models.ForeignKey(Videojuego, on_delete=models.CASCADE)
    precio = models.FloatField()
    stock = models.IntegerField()

class StockConsola(models.Model):
    tienda_id = models.ForeignKey(Tienda, on_delete=models.CASCADE)
    consola_id = models.ForeignKey(Consola, on_delete=models.CASCADE)
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
    tienda_id = models.ForeignKey(Tienda, on_delete=models.CASCADE)
    


class Trabajador(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    usuario = models.CharField(max_length=50)
    tienda_id = models.ForeignKey(Tienda, on_delete=models.CASCADE)
    administrador_id = models.ForeignKey(Administrador, on_delete=models.CASCADE)

class ReservaVideojuego(models.Model):
    estadoNoCompletada = 'No completada'
    estadoCompletada = 'Completada'
    ESTADOS = {
    (estadoCompletada, 'No completada'),
    (estadoNoCompletada, 'Completada')
}

    cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    stockVideojuego_id = models.ForeignKey(StockVideojuego, on_delete=models.CASCADE)
    fecha = models.DateField()
    estado = models.CharField(max_length=50, choices=ESTADOS)

class ReservaConsola(models.Model):
    estadoNoCompletada = 'No completada'
    estadoCompletada = 'Completada'
    ESTADOS = {
    (estadoCompletada, 'No completada'),
    (estadoNoCompletada, 'Completada')}
    
    cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    stockConsola_id = models.ForeignKey(StockConsola, on_delete=models.CASCADE)
    fecha = models.DateField()
    estado = models.CharField(max_length=50, choices=ESTADOS)
