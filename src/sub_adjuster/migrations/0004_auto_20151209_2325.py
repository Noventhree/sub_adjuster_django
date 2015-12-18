# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_adjuster', '0003_auto_20151208_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtitles',
            name='line_A',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='subtitles',
            name='line_B',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='subtitles',
            name='line_C',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
