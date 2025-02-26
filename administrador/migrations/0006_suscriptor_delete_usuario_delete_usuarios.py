# Generated by Django 4.2.2 on 2023-07-25 22:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("administrador", "0005_usuario_usuarios_delete_suscriptor"),
    ]

    operations = [
        migrations.CreateModel(
            name="Suscriptor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("nombre", models.CharField(max_length=100)),
                ("apellido", models.CharField(max_length=100)),
                ("clave", models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name="Usuario",
        ),
        migrations.DeleteModel(
            name="Usuarios",
        ),
    ]
