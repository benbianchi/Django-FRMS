# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0006_auto_20150326_2147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funding',
            name='requestSum',
        ),
        migrations.AddField(
            model_name='funding',
            name='requestinfo',
            field=models.TextField(default=1, max_length=512, verbose_name=b'Event Summary'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='funding',
            name='requestNumber',
            field=models.AutoField(serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
