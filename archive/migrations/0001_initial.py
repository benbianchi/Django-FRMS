# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField()),
                ('budgetAmount', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('clubID', models.AutoField(serialize=False, primary_key=True)),
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
        migrations.CreateModel(
            name='Portion',
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
        migrations.CreateModel(
            name='Request',
            fields=[
                ('Eventinfo', models.TextField(default=b'', max_length=512, verbose_name=b'Request Summary')),
                ('EventName', models.CharField(max_length=256, verbose_name=b'Request Name')),
                ('EventNumber', models.AutoField(serialize=False, primary_key=True)),
                ('clubID', models.ForeignKey(to='archive.Club')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='portion',
            name='requestNumber',
            field=models.ForeignKey(to='archive.Request'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='budget',
            name='clubID',
            field=models.ForeignKey(to='archive.Club'),
            preserve_default=True,
        ),
    ]
