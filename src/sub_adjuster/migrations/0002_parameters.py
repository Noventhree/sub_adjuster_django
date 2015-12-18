# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_adjuster', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parameters',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('initial_deley', models.FloatField(default=0)),
                ('multiplier', models.FloatField(default=1.0)),
            ],
        ),
    ]
