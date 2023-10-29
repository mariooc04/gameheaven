from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from gameheaven.Constantes import ConstantesVOs as Constantes

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

    def create_user(self, email, username, role, password=None):
        if not email:
            raise ValueError('El usuario debe tener un email')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        
        
        user.role = role
        user.set_password(password)
        user.save(using=self._db)

        
        return user
    
    def create_superuser(self, email, username, password=None):
        user = self.create_user(
            email,
            password=password,
            username=username,
            role=Usuario.Roles.ADMIN
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        
        return user
    
    def authenticate(self, request, email=None, password=None):
        try:
            user = self.model.objects.get(email=email)
        except self.model.DoesNotExist:
            return None
        
        if user.check_password(password):
            return user
        return None
    
class Usuario(AbstractBaseUser, PermissionsMixin):
    class Roles(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        CLIENTE = 'CLIENTE', 'Cliente'
        TRABAJADOR = 'TRABAJADOR', 'Trabajador'

    email = models.EmailField(max_length=50, unique=True)
    username = models.CharField(max_length=50, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    role = models.CharField(max_length=50, choices=Roles.choices, default=Roles.CLIENTE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
@receiver(post_save, sender=Usuario)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == Usuario.Roles.TRABAJADOR:
            trabajador_group = Group.objects.get(name=Constantes.GRUPO_TRABAJADORES)
            instance.groups.add(trabajador_group)
            Trabajador.objects.create(usuario=instance)
        elif instance.role == Usuario.Roles.CLIENTE:
            cliente_group = Group.objects.get(name=Constantes.GRUPO_CLIENTES)
            instance.groups.add(cliente_group)
            Cliente.objects.create(usuario=instance)
        
class Trabajador(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.user} trabajador en {self.tienda}'
        
class Cliente(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.user} cliente en {self.tienda}'

    
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
