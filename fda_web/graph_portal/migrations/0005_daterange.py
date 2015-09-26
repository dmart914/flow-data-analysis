# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graph_portal', '0004_auto_20150921_2319'),
    ]

    operations = [
        migrations.CreateModel(
            name='DateRange',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('daterange_from', models.DateTimeField()),
                ('daterange_to', models.DateTimeField()),
                ('daterange_meter_pk', models.ForeignKey(to='graph_portal.FlowMeter')),
            ],
        ),
    ]
