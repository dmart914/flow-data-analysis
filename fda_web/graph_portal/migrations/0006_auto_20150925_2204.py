# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graph_portal', '0005_daterange'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='daterange',
            name='daterange_meter_pk',
        ),
        migrations.DeleteModel(
            name='DateRange',
        ),
    ]
