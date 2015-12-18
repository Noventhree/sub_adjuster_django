# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_adjuster', '0011_auto_20151210_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtitles',
            name='line_A',
            field=models.CharField(default=None, max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='subtitles',
            name='line_B',
            field=models.CharField(default=None, max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='subtitles',
            name='line_C',
            field=models.CharField(default=None, max_length=255, blank=True),
        ),
    ]
