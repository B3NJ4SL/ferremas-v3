# Generated by Django 5.0.4 on 2024-05-24 01:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webSBLS', '0012_contacto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trabajo',
            old_name='mecanico',
            new_name='Usuarioreg',
        ),
    ]