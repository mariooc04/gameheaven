# Generated by Django 4.2.6 on 2023-10-25 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gameheaven', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='user',
            new_name='usuario',
        ),
        migrations.RenameField(
            model_name='trabajador',
            old_name='user',
            new_name='usuario',
        ),
    ]