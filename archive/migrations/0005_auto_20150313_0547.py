# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0004_requestportion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funding',
            fields=[
                ('requestSum', models.FloatField()),
                ('requestNumber', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='requestportion',
            name='requestNumber',
        ),
        migrations.DeleteModel(
            name='RequestPortion',
        ),
        migrations.AddField(
            model_name='request',
            name='requestNumber',
            field=models.ForeignKey(default=2, to='archive.Funding'),
            preserve_default=False,
        ),
    ]
