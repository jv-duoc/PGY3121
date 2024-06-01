# Generated by Django 4.2.13 on 2024-06-01 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('texto', models.CharField(max_length=1024)),
                ('completado', models.BooleanField(default=False)),
            ],
        ),
    ]
