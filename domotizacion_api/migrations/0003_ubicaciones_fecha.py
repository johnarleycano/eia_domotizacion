# Generated by Django 5.0.2 on 2024-02-29 22:44

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domotizacion_api', '0002_rename_usuario_id_ubicaciones_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='ubicaciones',
            name='fecha',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]