# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musico', '0003_auto_20161122_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cometario',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('cometario', models.TextField()),
                ('foto', models.ForeignKey(to='musico.Album')),
            ],
        ),
    ]
