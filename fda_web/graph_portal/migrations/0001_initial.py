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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('date', models.DateTimeField(verbose_name='date')),
                ('air_temp', models.FloatField()),
                ('inlet_depth', models.FloatField()),
                ('throat_depth', models.FloatField()),
                ('submergence', models.FloatField()),
                ('flow_rate', models.FloatField()),
                ('accumulated_flow', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FlowMeter',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=240)),
                ('meter_type', models.CharField(max_length=240, default='Unset Type')),
                ('gps_x', models.DecimalField(null=True, max_digits=12, blank=True, decimal_places=6)),
                ('gps_y', models.DecimalField(null=True, max_digits=12, blank=True, decimal_places=6)),
                ('addr_number', models.IntegerField(null=True, blank=True)),
                ('addr_street1', models.CharField(null=True, max_length=240, blank=True)),
                ('addr_street2', models.CharField(null=True, max_length=240, blank=True)),
                ('addr_city', models.CharField(null=True, max_length=240, blank=True)),
                ('addr_state', models.CharField(null=True, max_length=30, blank=True)),
                ('addr_country', models.CharField(null=True, max_length=240, blank=True)),
                ('last_service', models.DateField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UploadFile',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('file', models.FileField(upload_to='/home/dave/flow-data-analysis/fda_web/files')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='datapoint',
            name='flow_meter',
            field=models.ForeignKey(to='graph_portal.FlowMeter', default=1),
            preserve_default=True,
        ),
    ]
