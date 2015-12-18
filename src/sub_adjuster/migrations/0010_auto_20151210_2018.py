# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_adjuster', '0009_auto_20151210_2016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subtitles',
            name='line_A',
        ),
        migrations.RemoveField(
            model_name='subtitles',
            name='line_B',
        ),
        migrations.RemoveField(
            model_name='subtitles',
            name='line_C',
        ),
    ]
