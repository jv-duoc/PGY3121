# Generated by Django 4.2.13 on 2024-05-25 01:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_automotora', '0002_auto_fecha_alter_auto_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='fecha',
            field=models.DateTimeField(default=datetime.date(2024, 5, 25), editable=False),
        ),
    ]