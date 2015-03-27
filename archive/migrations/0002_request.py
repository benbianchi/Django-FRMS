# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('requestAmount', models.FloatField()),
                ('requestDescription', models.TextField()),
                ('outcome', models.TextField()),
                ('reviewDate', models.DateField()),
                ('requestType', models.IntegerField(default=1, choices=[(1, b'Funding Request'), (2, b'Sponsorship')])),
                ('clubID', models.ForeignKey(to='archive.Club')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
