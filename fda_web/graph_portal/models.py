from django.db import models
from django import forms

from datetime import datetime

import pytz

DEFAULT_PK = 1

class FlowMeter(models.Model):
    name = models.CharField(max_length=240)

    def __str__(self):
        return self.name


class DataPointCreator(models.Manager):
    def create_datapoint(self, line):
        line_arr = line.split(',')
        west_tz = pytz.timezone('America/Los_Angeles')
        naive_date = datetime.strptime(line_arr[1], ' %m/%d/%Y %H:%M:%S')
        aware_date = naive_date.replace(tzinfo=west_tz)
        dp = self.create(
            date=aware_date,
            air_temp=float(line_arr[2]),
            inlet_depth=float(line_arr[3]),
            throat_depth=float(line_arr[4]),
            submergence=float(line_arr[5]),
            flow_rate=float(line_arr[6]),
            accumulated_flow=float(line_arr[7])
        )
        return dp


class DataPoint(models.Model):
    flow_meter = models.ForeignKey(FlowMeter, default=DEFAULT_PK)
    date = models.DateTimeField('date')
    air_temp = models.FloatField()
    inlet_depth = models.FloatField()
    throat_depth = models.FloatField()
    submergence = models.FloatField()
    flow_rate = models.FloatField()
    accumulated_flow = models.FloatField()

    def __str__(self):
        return self.flow_meter.name + ' - ' + str(self.date)

    objects = DataPointCreator()


class UploadFile(models.Model):
    ''' Reference: https://amatellanes.wordpress.com/2013/11/05/dropzonejs-django-how-to-build-a-file-upload-form/
    '''
    file = models.FileField(upload_to='files')


class UploadFileForm(forms.ModelForm):

    class Meta:
        model = UploadFile
        fields = ['file']
