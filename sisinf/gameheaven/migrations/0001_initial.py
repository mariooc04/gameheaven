# Generated by Django 4.2.6 on 2023-10-21 17:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('role', models.CharField(choices=[('ADMIN', 'Admin'), ('CLIENTE', 'Cliente'), ('TRABAJADOR', 'Trabajador')], default='CLIENTE', max_length=50)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Consola',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('descripcion', models.TextField(max_length=500, null=True)),
                ('valoracion', models.FloatField(null=True)),
                ('img', models.ImageField(null=True, upload_to='img/')),
            ],
        ),
        migrations.CreateModel(
            name='StockConsola',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.FloatField()),
                ('stock', models.IntegerField()),
                ('consola', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gameheaven.consola')),
            ],
        ),
        migrations.CreateModel(
            name='StockVideojuego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.FloatField()),
                ('stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Videojuego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('descripcion', models.TextField(max_length=500, null=True)),
                ('valoracion', models.FloatField(null=True)),
                ('plataformas', models.CharField(max_length=50, null=True)),
                ('img', models.ImageField(null=True, upload_to='img/')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tienda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciudad', models.CharField(max_length=50)),
                ('codigoPostal', models.IntegerField(unique=True)),
                ('consolas', models.ManyToManyField(through='gameheaven.StockConsola', to='gameheaven.consola')),
                ('videojuegos', models.ManyToManyField(through='gameheaven.StockVideojuego', to='gameheaven.videojuego')),
            ],
        ),
        migrations.AddField(
            model_name='stockvideojuego',
            name='tienda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gameheaven.tienda'),
        ),
        migrations.AddField(
            model_name='stockvideojuego',
            name='videojuego',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gameheaven.videojuego'),
        ),
        migrations.AddField(
            model_name='stockconsola',
            name='tienda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gameheaven.tienda'),
        ),
        migrations.CreateModel(
            name='ReservaVideojuego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('estado', models.CharField(choices=[('Completada', 'No completada'), ('No completada', 'Completada')], max_length=50)),
                ('stockVideojuego', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gameheaven.stockvideojuego')),
            ],
        ),
        migrations.CreateModel(
            name='ReservaConsola',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('estado', models.CharField(choices=[('Completada', 'No completada'), ('No completada', 'Completada')], max_length=50)),
                ('stockConsola', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gameheaven.stockconsola')),
            ],
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('tienda', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gameheaven.tienda')),
            ],
        ),
        migrations.AddConstraint(
            model_name='stockvideojuego',
            constraint=models.UniqueConstraint(fields=('tienda', 'videojuego'), name='unique_videojuego_tienda'),
        ),
        migrations.AddConstraint(
            model_name='stockconsola',
            constraint=models.UniqueConstraint(fields=('tienda', 'consola'), name='unique_consola_tienda'),
        ),
        migrations.AddField(
            model_name='reservavideojuego',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gameheaven.cliente'),
        ),
        migrations.AddField(
            model_name='reservaconsola',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gameheaven.cliente'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='tienda',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gameheaven.tienda'),
        ),
    ]
