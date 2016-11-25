# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musico', '0008_auto_20161122_1054'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cometario2',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('cometario', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='musico',
            name='foto',
            field=models.ImageField(default=1, upload_to='musicos/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='musico',
            name='apellido',
            field=models.CharField(default='Apellidos', max_length=50),
        ),
        migrations.AlterField(
            model_name='musico',
            name='correo',
            field=models.CharField(default='Correo', max_length=50),
        ),
        migrations.AlterField(
            model_name='musico',
            name='direccion',
            field=models.CharField(default='Dirección', max_length=80),
        ),
        migrations.AlterField(
            model_name='musico',
            name='fecha_nacimiento',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='musico',
            name='instrumento',
            field=models.CharField(default='Instrumento', max_length=100),
        ),
        migrations.AlterField(
            model_name='musico',
            name='nombre',
            field=models.CharField(default='Nombre', max_length=50),
        ),
        migrations.AlterField(
            model_name='musico',
            name='telefono',
            field=models.CharField(default='Télefono', max_length=15),
        ),
        migrations.AddField(
            model_name='cometario2',
            name='foto',
            field=models.ForeignKey(to='musico.Musico'),
        ),
    ]
