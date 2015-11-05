# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('graph_portal', '0001_initial'), ('graph_portal', '0002_auto_20150919_2234'), ('graph_portal', '0003_uploadfile'), ('graph_portal', '0004_auto_20150921_2319'), ('graph_portal', '0005_daterange'), ('graph_portal', '0006_auto_20150925_2204')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataPoint',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='date')),
                ('air_temp', models.FloatField()),
                ('inlet_depth', models.FloatField()),
                ('throat_depth', models.FloatField()),
                ('submergence', models.FloatField()),
                ('flow_rate', models.FloatField()),
                ('accumulated_flow', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='FlowMeter',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=240)),
            ],
        ),
        migrations.AddField(
            model_name='datapoint',
            name='flow_meter',
            field=models.ForeignKey(default=1, to='graph_portal.FlowMeter'),
        ),
        migrations.CreateModel(
            name='UploadFile',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('file', models.FileField(upload_to='/home/pi/flow-data-analysis/files')),
            ],
        ),
    ]
