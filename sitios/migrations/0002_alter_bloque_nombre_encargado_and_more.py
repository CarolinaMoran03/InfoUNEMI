# Generated by Django 4.2.2 on 2023-07-12 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloque',
            name='nombre_encargado',
            field=models.CharField(blank=True, max_length=100, verbose_name='Nombre del encargado'),
        ),
        migrations.AlterField(
            model_name='bloque',
            name='numero_planta',
            field=models.IntegerField(verbose_name='numero de plantas'),
        ),
    ]