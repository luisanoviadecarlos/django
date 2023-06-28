# Generated by Django 4.2.2 on 2023-06-22 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='productos',
            fields=[
                ('id_producto', models.CharField(max_length=60, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.TextField(max_length=50)),
                ('valor_producto', models.CharField(max_length=100)),
                ('fecha_ingreso', models.DateField()),
            ],
        ),
    ]
