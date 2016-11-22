# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musico', '0005_album_favorito'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='descripcion',
            field=models.TextField(default='Sin Descripcion'),
        ),
        migrations.AlterField(
            model_name='album',
            name='titulo',
            field=models.CharField(max_length=100, default='Sin titulo'),
        ),
    ]
