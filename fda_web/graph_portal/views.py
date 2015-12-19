from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from .models import *

def index(request):
    return render(request, 'graph_portal/index.html')


def meter_detail(request, meter_pk):
    meter = FlowMeter.objects.get(pk=meter_pk)
    dps = meter.datapoint_set.all()
    dps_count = dps.count()
    paginator = Paginator(dps, 100)

    page = request.GET.get('page')
    try:
        datapoints = paginator.page(page)
    except PageNotAnInteger:
        datapoints = paginator.page(1)
    except EmptyPage:
        datapoints = paginator.page(paginator.num_pages)

    return render_to_response('graph_portal/meter_detail.html', {
        'meter':meter, 
        'datapoints':datapoints,
        'datapoints_count':dps_count,
    })


def meter_create(request):
    if request.method == "POST":
        new_meter_form = FlowMeterForm(request.POST)

        if new_meter_form.is_valid():
            new_meter = new_meter_form.save()
            return redirect('graph_portal:meter_detail', meter_pk=new_meter.pk)

    else:
        new_meter_form = FlowMeterForm()

    return render(request, 'graph_portal/meter_create.html', {'new_meter_form' : new_meter_form})


def meter_edit(request, meter_pk):
    # Change this in to a get or 404
    meter = FlowMeter.objects.get(pk=meter_pk)
    
    if request.method == "POST":
        meter_form = FlowMeterForm(request.POST, instance=meter) 

        if meter_form.is_valid():            
            meter_form.save()
            messages.add_message(request, messages.SUCCESS, 'Meter edited')
            return redirect('graph_portal:meter_detail', meter_pk = meter.pk)

        else:
            messages.add_message(request, messages.ERROR, 'There was a problem with your edits')

    else:
        meter_form = FlowMeterForm(instance=meter)

    return render(request, 'graph_portal/meter_edit.html', {'meter': meter, 'form': meter_form})


def flow_meter_upload(request):
    meters = FlowMeter.objects.all()
    return render(request, 'graph_portal/meters.html', {'meters': meters})


def upload(request, meter_pk):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            new_file = UploadFile(file = request.FILES['file'])
            new_file.save()

            return HttpResponseRedirect(reverse('graph_portal:process', args=[meter_pk, str(new_file.pk)]))
    else:
        form = UploadFileForm()

    data = {'form': form, 'meter_pk':meter_pk}
    return render_to_response('graph_portal/upload.html', data, context_instance=RequestContext(request))


def process(request, meter_pk, file_pk):
    file = UploadFile.objects.get(pk=file_pk)

    # counters
    new_rows = 0
    bad_rows = 0
    dup_rows = 0

    with open(str(file.file)) as data_file:
        # Check the first line for proper formatting
        first_line = next(data_file)
        if first_line != 'Time since reset, Log Time, Air Temp, Inlet Depth, Throat Depth, Submergence, Flow Rate, Accumulated Flow\n':
            file.file_delete()
            file.delete()
            del file
            # raise AssertionError('Bad file header')
            return HttpResponse('Error: bad file header.')

        # iterate through the file
        for row in data_file:
            line_arr = row.split(',')
            try:
                aDataPoint = DataPoint.objects.create_datapoint(str(row), meter_pk)
                new_rows += 1
            except AssertionError:
                bad_rows += 1
            except FileExistsError:
                dup_rows += 1

    # delete file after processing
    file.file_delete()
    file.delete()
    del file

    output = 'New: ' + str(new_rows) + ' / Duplicates: ' + str(dup_rows) + ' / Bad rows: ' + str(bad_rows)

    return HttpResponse(output)


def graph_creation(request, meter_pk):
    if request.method == 'POST':
        form = DateRangeForm(request.POST)
        if form.is_valid():
            ''' TO DO:
                * Get datapoints between the date ranges
                * Import MatPlotLib
                * create graphs
                * display graphs on the page
                * add coniditional block for form errors
                * add jquery datetime selector
                * add some logic to destroy previous images?
                '''
            return HttpResponse(form);

    else:
        form = DateRangeForm()

    return render(request, 'graph_portal/graph_creation.html', {'form':form, 'meter_pk':meter_pk})
