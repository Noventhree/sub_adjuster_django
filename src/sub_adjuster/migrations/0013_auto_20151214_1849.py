# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_adjuster', '0012_auto_20151214_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtitles',
            name='line_A',
            field=models.CharField(blank=True, default='1', max_length=255),
        ),
        migrations.AlterField(
            model_name='subtitles',
            name='line_B',
            field=models.CharField(blank=True, default='1', max_length=255),
        ),
        migrations.AlterField(
            model_name='subtitles',
            name='line_C',
            field=models.CharField(blank=True, default='1', max_length=255),
        ),
    ]
