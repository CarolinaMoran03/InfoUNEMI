# Generated by Django 4.2.3 on 2023-07-31 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitios', '0014_remove_sitio_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitio',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='bloque_imagenes/'),
        ),
    ]
