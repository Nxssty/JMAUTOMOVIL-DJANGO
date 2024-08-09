# Generated by Django 5.0.7 on 2024-08-05 07:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autos',
            name='imagen',
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='autos/')),
                ('auto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagenes', to='core.autos')),
            ],
        ),
    ]
