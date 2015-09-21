from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse
from .models import *

def index(request):
    return render(request, 'graph_portal/index.html')

def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            new_file = UploadFile(file = request.FILES['file'])
            new_file.save()

            return HttpResponseRedirect(reverse('graph_portal:index'))
    else:
        form = UploadFileForm()

    data = {'form': form}
    return render_to_response('graph_portal/upload.html', data, context_instance=RequestContext(request))
