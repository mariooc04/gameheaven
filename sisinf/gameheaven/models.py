from django.db import models

# Create your models here.
class Tienda(models.Model):
    ciudad = models.CharField(max_length=50)
    codigoPostal = models.IntegerField()
    videojuegos = models.ManyToManyField('Videojuego', through='StockVideojuego')
    consolas = models.ManyToManyField('Consola', through='StockConsola')

    def __str__(self):
        return f'Tienda en {self.ciudad}, {self.codigoPostal}'
    

class Videojuego(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(max_length=500, null=True)
    valoracion = models.FloatField(null=True)
    plataformas = models.CharField(max_length=50, null=True)
    img = models.ImageField(upload_to='img/', null=True)

    def __str__(self):
        return f'Videojuego {self.nombre}'
    
    
class Consola(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(max_length=500, null=True)
    valoracion = models.FloatField(null=True)
    img = models.ImageField(upload_to='img/', null=True)

    def __str__(self):
        return f'Consola {self.nombre}'
    

class StockVideojuego(models.Model):
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)
    videojuego = models.ForeignKey(Videojuego, on_delete=models.CASCADE)
    precio = models.FloatField()
    stock = models.IntegerField()

    class Meta:
        unique_together = ('tienda', 'videojuego')


    def __str__(self):
        return f'Videojuego {self.videojuego} en tienda {self.tienda}, precio {self.precio} €, stock {self.stock}'

class StockConsola(models.Model):
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)
    consola = models.ForeignKey(Consola, on_delete=models.CASCADE)
    precio = models.FloatField()
    stock = models.IntegerField()

    class Meta:
        unique_together = ('tienda', 'consola')


    def __str__(self):
        return f'Consola {self.consola} en tienda {self.tienda}, precio {self.precio} €, stock {self.stock}'

class Administrador(models.Model):
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    usuario = models.CharField(max_length=50)

    def __str__(self):
        return f'Administrador {self.usuario}'

class Cliente(models.Model):
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    usuario = models.CharField(max_length=50)
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)

    def __str__(self):
        return f'Cliente {self.usuario}'
    


class Trabajador(models.Model):
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    usuario = models.CharField(max_length=50)
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)
    administrador = models.ForeignKey(Administrador, on_delete=models.CASCADE)

    def __str__(self):
        return f'Trabajador {self.usuario}'

class ReservaVideojuego(models.Model):
    estadoNoCompletada = 'No completada'
    estadoCompletada = 'Completada'
    ESTADOS = {
    (estadoCompletada, 'No completada'),
    (estadoNoCompletada, 'Completada')}

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    stockVideojuego = models.ForeignKey(StockVideojuego, on_delete=models.CASCADE)
    fecha = models.DateField()
    estado = models.CharField(max_length=50, choices=ESTADOS)

    def __str__(self):
        return f'Reserva de {self.stockVideojuego} por {self.cliente}'

class ReservaConsola(models.Model):
    estadoNoCompletada = 'No completada'
    estadoCompletada = 'Completada'
    ESTADOS = {
    (estadoCompletada, 'No completada'),
    (estadoNoCompletada, 'Completada')}
    
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    stockConsola = models.ForeignKey(StockConsola, on_delete=models.CASCADE)
    fecha = models.DateField()
    estado = models.CharField(max_length=50, choices=ESTADOS)

    def __str__(self):
        return f'Reserva de {self.stockConsola} por {self.cliente}'
