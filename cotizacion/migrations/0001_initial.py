# Generated by Django 4.2.3 on 2023-07-27 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cliente",
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
                ("nombre", models.CharField(max_length=100)),
                ("direccion", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Color",
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
                ("color", models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name="DetallePresupuesto",
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
                ("cantidad", models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name="Insumo",
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
                ("nombre", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Tipo",
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
                ("tipo", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Ventana",
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
                ("ancho", models.DecimalField(decimal_places=2, max_digits=5)),
                ("alto", models.DecimalField(decimal_places=2, max_digits=5)),
                (
                    "color",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cotizacion.color",
                    ),
                ),
                (
                    "tipo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cotizacion.tipo",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Presupuesto",
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
                (
                    "numero_presupuesto",
                    models.PositiveBigIntegerField(blank=True, null=True, unique=True),
                ),
                (
                    "cliente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cotizacion.cliente",
                    ),
                ),
                (
                    "ventanas",
                    models.ManyToManyField(
                        through="cotizacion.DetallePresupuesto", to="cotizacion.ventana"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="detallepresupuesto",
            name="presupuesto",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="cotizacion.presupuesto"
            ),
        ),
        migrations.AddField(
            model_name="detallepresupuesto",
            name="ventana",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="cotizacion.ventana"
            ),
        ),
    ]