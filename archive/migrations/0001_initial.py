# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('clubID', models.IntegerField(default=0, serialize=False, primary_key=True)),
                ('officerAlias', models.CharField(default=b'', max_length=50, verbose_name=b'Officer Email Alias')),
                ('shortName', models.CharField(default=b'', max_length=20, verbose_name=b'Colloquial Name for Club')),
                ('numMembers', models.IntegerField(default=0, verbose_name=b'Number of Active Members')),
                ('clubPurpose', models.TextField(default=b'', max_length=256, verbose_name=b"Club's Purpose")),
                ('clubClass', models.IntegerField(default=1, max_length=2, verbose_name=b'Club Class', choices=[(1, b'Special Interest'), (2, b'Club Sports'), (3, b'Campus Wide'), (4, b'Selective Membership'), (5, b'Greek-life'), (6, b'Provinsial')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
