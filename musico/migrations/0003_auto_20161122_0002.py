# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musico', '0002_album_foto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='artista',
            new_name='musico',
        ),
        migrations.AlterField(
            model_name='album',
            name='foto',
            field=models.ImageField(upload_to='/fotografias/'),
        ),
    ]
