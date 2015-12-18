# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_adjuster', '0004_auto_20151209_2325'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subtitles',
            old_name='file',
            new_name='sub_file',
        ),
    ]
