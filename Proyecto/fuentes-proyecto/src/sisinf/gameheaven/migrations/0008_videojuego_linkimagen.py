# Generated by Django 4.2.6 on 2023-11-17 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameheaven', '0007_videojuego_steamid'),
    ]

    operations = [
        migrations.AddField(
            model_name='videojuego',
            name='linkImagen',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
