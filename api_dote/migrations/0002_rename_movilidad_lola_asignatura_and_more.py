# Generated by Django 4.1.3 on 2022-11-26 03:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_dote', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lola',
            old_name='movilidad',
            new_name='asignatura',
        ),
        migrations.RenameField(
            model_name='lola',
            old_name='correos',
            new_name='correo',
        ),
        migrations.RenameField(
            model_name='lola',
            old_name='rut',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='lola',
            old_name='nombres',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='lola',
            old_name='ticket',
            new_name='telefono',
        ),
        migrations.RemoveField(
            model_name='lola',
            name='apellidos',
        ),
    ]
