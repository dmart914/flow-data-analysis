# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graph_portal', '0001_squashed_0006_auto_20150925_2204'),
    ]

    operations = [
        migrations.AddField(
            model_name='flowmeter',
            name='addr_city',
            field=models.CharField(null=True, blank=True, max_length=240),
        ),
        migrations.AddField(
            model_name='flowmeter',
            name='addr_country',
            field=models.CharField(null=True, blank=True, max_length=240),
        ),
        migrations.AddField(
            model_name='flowmeter',
            name='addr_number',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='flowmeter',
            name='addr_state',
            field=models.CharField(null=True, blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='flowmeter',
            name='addr_street1',
            field=models.CharField(null=True, blank=True, max_length=240),
        ),
        migrations.AddField(
            model_name='flowmeter',
            name='addr_street2',
            field=models.CharField(null=True, blank=True, max_length=240),
        ),
        migrations.AddField(
            model_name='flowmeter',
            name='gps_x',
            field=models.DecimalField(null=True, blank=True, decimal_places=6, max_digits=12),
        ),
        migrations.AddField(
            model_name='flowmeter',
            name='gps_y',
            field=models.DecimalField(null=True, blank=True, decimal_places=6, max_digits=12),
        ),
        migrations.AddField(
            model_name='flowmeter',
            name='last_service',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='flowmeter',
            name='meter_type',
            field=models.CharField(default='Unset Type', max_length=240),
        ),
    ]
