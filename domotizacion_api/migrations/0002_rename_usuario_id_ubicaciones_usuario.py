# Generated by Django 5.0.2 on 2024-02-24 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('domotizacion_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ubicaciones',
            old_name='usuario_id',
            new_name='usuario',
        ),
    ]
