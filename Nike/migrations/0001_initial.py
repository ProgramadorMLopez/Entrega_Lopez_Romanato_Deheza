# Generated by Django 4.0.4 on 2022-06-05 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='accesorios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_barra', models.CharField(max_length=40, unique=True)),
                ('nombre', models.CharField(max_length=40)),
                ('precio', models.FloatField()),
                ('color', models.CharField(max_length=40)),
                ('cod_categoria', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='calzados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_barra', models.CharField(max_length=40, unique=True)),
                ('nombre', models.CharField(max_length=40)),
                ('precio', models.FloatField()),
                ('talle', models.CharField(max_length=40)),
                ('color', models.CharField(max_length=40)),
                ('cod_categoria', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='indumentarias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_barra', models.CharField(max_length=40, unique=True)),
                ('nombre', models.CharField(max_length=40)),
                ('precio', models.FloatField()),
                ('talle', models.CharField(max_length=40)),
                ('color', models.CharField(max_length=40)),
                ('cod_estacion', models.IntegerField()),
            ],
        ),
    ]
