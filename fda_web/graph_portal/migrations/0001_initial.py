# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataPoint',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='date')),
                ('air_temp', models.FloatField()),
                ('inlet_depth', models.FloatField()),
                ('throat_depth', models.FloatField()),
                ('submergence', models.FloatField()),
                ('flow_rate', models.FloatField()),
                ('accumulated_flow', models.FloatField()),
            ],
        ),
    ]
