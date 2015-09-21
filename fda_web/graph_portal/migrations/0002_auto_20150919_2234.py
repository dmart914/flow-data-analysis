# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graph_portal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlowMeter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=240)),
            ],
        ),
        migrations.AddField(
            model_name='datapoint',
            name='flow_meter',
            field=models.ForeignKey(default=1, to='graph_portal.FlowMeter'),
        ),
    ]
