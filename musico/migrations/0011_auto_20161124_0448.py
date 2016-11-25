# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musico', '0010_auto_20161124_0446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musico',
            name='fecha_nacimiento',
            field=models.DateField(default='01/01/0000'),
        ),
    ]
