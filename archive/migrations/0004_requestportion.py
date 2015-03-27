# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0003_budget'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestPortion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('portionAllocated', models.FloatField()),
                ('requestNumber', models.ForeignKey(to='archive.Request')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
