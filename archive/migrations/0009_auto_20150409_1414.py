# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0008_auto_20150329_2019'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('Eventinfo', models.TextField(default=b'', max_length=512, verbose_name=b'Event Summary')),
                ('EventName', models.CharField(max_length=256, verbose_name=b'Event Name')),
                ('EventNumber', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='request',
            name='requestNumber',
            field=models.ForeignKey(to='archive.Event'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Funding',
        ),
    ]
