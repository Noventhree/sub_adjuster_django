# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_adjuster', '0006_auto_20151210_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtitles',
            name='sub_file',
            field=models.FileField(upload_to='.'),
        ),
    ]
