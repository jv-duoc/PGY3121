# Generated by Django 5.0.6 on 2024-06-01 00:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_automotora', '0008_alter_auto_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='auto',
            name='tipo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='web_automotora.tipo'),
        ),
    ]
