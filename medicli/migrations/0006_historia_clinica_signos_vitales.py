# Generated by Django 4.1.1 on 2022-09-18 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicli', '0005_diagnostico_familiar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Historia_clinica',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Fecha_Toma', models.DateField()),
                ('Sugerencia', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Signos_vitales',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Fecha_Toma', models.DateField()),
                ('Oximetria', models.CharField(max_length=20)),
                ('Frecuencia_Respiraoria', models.CharField(max_length=20)),
                ('Frecuencia_cardiaca', models.CharField(max_length=20)),
                ('Temperatura', models.CharField(max_length=20)),
                ('Presion_Arterial', models.CharField(max_length=20)),
                ('Glicemia', models.CharField(max_length=20)),
            ],
        ),
    ]