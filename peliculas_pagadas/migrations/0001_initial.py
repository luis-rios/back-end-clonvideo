# Generated by Django 2.2.14 on 2021-03-19 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categorias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pelicula_pagada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('category', models.CharField(max_length=200)),
                ('img', models.CharField(max_length=200)),
                ('duration', models.TimeField()),
                ('language', models.CharField(max_length=200)),
                ('subtitles', models.CharField(max_length=200)),
                ('creationDate', models.DateField(auto_now=True)),
                ('classification', models.IntegerField()),
                ('link', models.CharField(max_length=200)),
                ('rent', models.IntegerField()),
                ('buy', models.IntegerField()),
                ('direction', models.CharField(max_length=100)),
                ('distribution', models.CharField(max_length=200)),
                ('categories', models.ManyToManyField(related_name='Pelicula_pagada', to='categorias.Categoria')),
            ],
        ),
    ]
