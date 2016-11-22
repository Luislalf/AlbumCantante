# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musico', '0004_cometario'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='favorito',
            field=models.BooleanField(default=False),
        ),
    ]
