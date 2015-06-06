# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0002_request_eventdate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('chartType', models.IntegerField(default=1, choices=[(1, b'Line'), (2, b'Pie'), (3, b'Bar'), (4, b'Column')])),
                ('chartTitle', models.TextField(max_length=256)),
            ],
        ),
    ]
