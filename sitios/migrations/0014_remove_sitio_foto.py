# Generated by Django 4.2.3 on 2023-07-31 04:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitios', '0013_rename_imagen_sitio_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitio',
            name='foto',
        ),
    ]
