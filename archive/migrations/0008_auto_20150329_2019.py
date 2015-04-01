# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0007_auto_20150327_1302'),
    ]

    operations = [
        migrations.AddField(
            model_name='funding',
            name='requestName',
            field=models.CharField(default='', max_length=256, verbose_name=b'Event Name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='funding',
            name='requestinfo',
            field=models.TextField(default=b'', max_length=512, verbose_name=b'Event Summary'),
            preserve_default=True,
        ),
    ]
