# Generated by Django 4.2.2 on 2023-07-12 03:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bloque',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre del bloque')),
                ('funciones', models.CharField(max_length=100, verbose_name='Funciones del Bloque')),
                ('nombre_encargado', models.CharField(max_length=100, verbose_name='Nombre del encargado')),
                ('numero_planta', models.IntegerField(verbose_name='numero de plantas ')),
                ('horario_bloque', models.CharField(max_length=100, verbose_name='Horarios')),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Bloque',
                'verbose_name_plural': 'Bloques',
            },
        ),
        migrations.CreateModel(
            name='Sitio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre del Sitio')),
                ('horario', models.CharField(max_length=100, verbose_name='Horario de atencion')),
                ('foto', models.URLField(verbose_name='foto')),
                ('gps', models.CharField(max_length=100)),
                ('Bloques', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='sitios.bloque')),
            ],
            options={
                'verbose_name': 'Sitio',
                'verbose_name_plural': 'Sitios',
            },
        ),
    ]