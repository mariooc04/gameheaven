from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

class Tienda(models.Model):
    ciudad = models.CharField(max_length=50)
    codigoPostal = models.IntegerField(unique=True)
    videojuegos = models.ManyToManyField('Videojuego', through='StockVideojuego')
    consolas = models.ManyToManyField('Consola', through='StockConsola')

    def __str__(self):
        return f'{self.ciudad}, {self.codigoPostal}'
    
#Productos

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
    
#Stock

class StockVideojuego(models.Model):
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)
    videojuego = models.ForeignKey(Videojuego, on_delete=models.CASCADE)
    precio = models.FloatField()
    stock = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['tienda', 'videojuego'], name='unique_videojuego_tienda')
        ]


    def __str__(self):
        return f'Videojuego {self.videojuego} en tienda {self.tienda}, precio {self.precio} €, stock {self.stock}'

class StockConsola(models.Model):
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)
    consola = models.ForeignKey(Consola, on_delete=models.CASCADE)
    precio = models.FloatField()
    stock = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['tienda', 'consola'], name='unique_consola_tienda')
        ]

    def __str__(self):
        return f'Consola {self.consola} en tienda {self.tienda}, precio {self.precio} €, stock {self.stock}'


#Usuarios

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True or extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_staff=True and is_superuser=True.')
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        TRABAJADOR = "TRABAJADOR", "Trabajador"
        CLIENTE = "CLIENTE", "Cliente"

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=30, blank=True)
    role = models.CharField(max_length=50, choices=Role.choices, default=Role.ADMIN)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.Role.ADMIN
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.email

CustomUser._meta.get_field('groups').related_name = 'customuser_set'

class Trabajador(CustomUser):
    def save(self, *args, **kwargs):
        self.role = CustomUser.Role.TRABAJADOR
        super().save(*args, **kwargs)

class Cliente(CustomUser):
    def save(self, *args, **kwargs):
        self.role = CustomUser.Role.CLIENTE
        super().save(*args, **kwargs)

class TrabajadorProfile(models.Model):
    user = models.OneToOneField(Trabajador, on_delete=models.CASCADE)
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)

class ClienteProfile(models.Model):
    user = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    tienda = models.ForeignKey(Tienda, null=True, on_delete=models.SET_NULL)
 
    
#Reservas

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
