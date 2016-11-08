# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('titulo', models.CharField(max_length=100)),
                ('fecha_lanzamiento', models.DateField()),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Musico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('instrumento', models.CharField(max_length=100, default='Sin instrumento')),
                ('fecha_nacimiento', models.DateField()),
                ('direccion', models.CharField(max_length=80)),
                ('telefono', models.CharField(max_length=15)),
                ('correo', models.CharField(max_length=50)),
                ('fecha_ingreso', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='artista',
            field=models.ForeignKey(to='musico.Musico'),
        ),
        migrations.AddField(
            model_name='album',
            name='autor',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
