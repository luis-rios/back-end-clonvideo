# Generated by Django 2.2.14 on 2021-03-18 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categorias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('img', models.CharField(max_length=200)),
                ('seasons', models.IntegerField()),
                ('languages', models.CharField(max_length=200)),
                ('subtitles', models.CharField(max_length=200)),
                ('creationDate', models.TimeField()),
                ('classification', models.IntegerField()),
                ('link', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('distribution', models.CharField(max_length=200)),
                ('direction', models.CharField(max_length=200)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Serie', to='categorias.Categoria')),
            ],
        ),
    ]
