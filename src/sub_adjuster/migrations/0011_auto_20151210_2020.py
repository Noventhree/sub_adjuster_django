# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_adjuster', '0010_auto_20151210_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='subtitles',
            name='line_A',
            field=models.CharField(default='1', blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='subtitles',
            name='line_B',
            field=models.CharField(default='1', blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='subtitles',
            name='line_C',
            field=models.CharField(default='1', blank=True, max_length=255),
        ),
    ]
