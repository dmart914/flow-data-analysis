from django.db import models


class DataPoint(models.Model):
    date = models.DateTimeField('date')
    air_temp = models.FloatField()
    inlet_depth = models.FloatField()
    throat_depth = models.FloatField()
    submergence = models.FloatField()
    flow_rate = models.FloatField()
    accumulated_flow = models.FloatField()

