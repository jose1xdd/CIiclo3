# Generated by Django 4.1.1 on 2022-09-19 03:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicli', '0008_rename_fecha_toma_signos_vitales_fecha_toma_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signos_vitales',
            old_name='Frecuencia_cardiaca',
            new_name='frecuencia_cardiaca',
        ),
    ]
