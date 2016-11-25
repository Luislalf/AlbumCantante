# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musico', '0012_auto_20161124_0449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='fecha_lanzamiento',
            field=models.DateField(default='01/01/2016'),
        ),
    ]
