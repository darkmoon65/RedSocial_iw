# Generated by Django 4.2.6 on 2023-10-31 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_alter_usuario_imagen_perfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='imagen_perfil',
            field=models.ImageField(blank=True, null=True, upload_to='apps/usuarios/imagenesPerfil/'),
        ),
    ]
