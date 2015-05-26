# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='EventDate',
            field=models.DateField(default=datetime.datetime(2015, 5, 24, 4, 54, 17, 817192, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
