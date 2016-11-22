# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musico', '0007_auto_20161122_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='foto',
            field=models.ImageField(upload_to='fotos/'),
        ),
    ]
