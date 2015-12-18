# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_adjuster', '0008_auto_20151210_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtitles',
            name='line_A',
            field=models.CharField(max_length=255, default='1', blank=True),
        ),
        migrations.AlterField(
            model_name='subtitles',
            name='line_B',
            field=models.CharField(max_length=255, default='1', blank=True),
        ),
        migrations.AlterField(
            model_name='subtitles',
            name='line_C',
            field=models.CharField(max_length=255, default='1', blank=True),
        ),
    ]
