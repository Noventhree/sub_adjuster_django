# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subtitles',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('file', models.FileField(upload_to='')),
                ('line_A', models.CharField(max_length=255)),
                ('line_B', models.CharField(max_length=255)),
                ('line_C', models.CharField(max_length=255)),
            ],
        ),
    ]
