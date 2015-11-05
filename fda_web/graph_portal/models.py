from django.db import models
from django import forms

from datetime import datetime

import pytz

DEFAULT_PK = 1

class FlowMeter(models.Model):
    ''' A meter that measures water '''

    name = models.CharField(max_length=240)
    meter_type = models.CharField(max_length=240, default="Unset Type")
    
    # Location info
    gps_x = models.DecimalField(max_digits=12, decimal_places=6, null=True, blank=True)
    gps_y = models.DecimalField(max_digits=12, decimal_places=6, null=True, blank=True)
    addr_number = models.IntegerField(null=True, blank=True)
    addr_street1 = models.CharField(max_length=240, null=True, blank=True)
    addr_street2 = models.CharField(max_length=240, null=True, blank=True)
    addr_city = models.CharField(max_length=240, null=True, blank=True)
    addr_state = models.CharField(max_length=30, null=True, blank=True)
    addr_country = models.CharField(max_length=240, null=True, blank=True)

    last_service = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class FlowMeterForm(forms.ModelForm):
    class Meta:
        model = FlowMeter
        fields = ['name','meter_type','gps_x','gps_y','addr_number','addr_street1','addr_street2','addr_city','addr_state','addr_country','last_service']


class DataPointCreator(models.Manager):
    def create_datapoint(self, line, target_pk=DEFAULT_PK):
        line_arr = line.split(',')

        if len(line_arr) != 8:
            raise AssertionError('Wrong number of columns')

        west_tz = pytz.timezone('America/Los_Angeles')
        naive_date = datetime.strptime(line_arr[1], ' %m/%d/%Y %H:%M:%S')
        aware_date = naive_date.replace(tzinfo=west_tz)

        # Check for duplicate datapoint
        # Note: this will reject any datapoint of any matching datetime.
        # This model should be refactored so it gets a pk of the flow_meter
        # it belongs to.
        # Conditional will be:
        if len(DataPoint.objects.filter(date=aware_date).filter(flow_meter=FlowMeter.objects.get(pk=target_pk))) > 0:
            raise FileExistsError('Record already exists')

        dp = self.create(
            flow_meter = FlowMeter.objects.get(pk=target_pk),
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

    from django.conf import settings
    rel_path = settings.BASE_DIR
    file = models.FileField(upload_to= rel_path + '/files')

    def file_delete(self):
        import os
        os.remove(str(self.file))

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFile
        fields = ['file']

class DateRangeForm(forms.Form):
    daterangemeter_pk = forms.ModelChoiceField(queryset=FlowMeter.objects.all(), label='Meter')
    daterange_from = forms.DateTimeField(label='Start date and time')
    daterange_to = forms.DateTimeField(label='End date and time')
