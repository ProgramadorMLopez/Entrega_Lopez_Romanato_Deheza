# Generated by Django 4.0.4 on 2022-07-05 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_usuario_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='imagen',
            field=models.ImageField(blank=True, default='default.jpg', max_length=200, null=True, upload_to='perfil/', verbose_name='Imagen de Perfil'),
        ),
    ]
