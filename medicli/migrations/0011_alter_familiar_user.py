# Generated by Django 4.1.1 on 2022-10-02 17:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medicli', '0010_alter_familiar_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familiar',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='familiar', to=settings.AUTH_USER_MODEL),
        ),
    ]
