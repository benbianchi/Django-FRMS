# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0005_auto_20150313_0547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='clubID',
            field=models.AutoField(serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
