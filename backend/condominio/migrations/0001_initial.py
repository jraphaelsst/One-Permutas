# Generated by Django 4.2.9 on 2024-02-04 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Condominio",
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
                ("nome", models.CharField(max_length=50)),
                ("cep", models.CharField(max_length=20)),
                ("estado", models.CharField(max_length=50)),
                ("cidade", models.CharField(max_length=50)),
                ("bairro", models.CharField(max_length=50)),
                ("endereco", models.CharField(max_length=100)),
                ("numero", models.PositiveIntegerField()),
                ("km", models.PositiveIntegerField()),
                ("valor_condominio", models.PositiveIntegerField()),
            ],
        ),
    ]
