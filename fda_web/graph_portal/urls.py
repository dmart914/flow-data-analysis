from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^meters/$', views.flow_meter_upload, name='meter_list'),
    url(r'^meters/create/$', views.meter_create, name='meter_create'),
    url(r'^meters/(?P<meter_pk>\d+)/edit/$', views.meter_edit, name='meter_edit'),
    
    url(r'^meters/(?P<meter_pk>\d+)/$', views.meter_detail, name='meter_detail'),
    url(r'^meters/(?P<meter_pk>\d+)/upload/$', views.upload, name='meter_upload'),
    url(r'^meters/(?P<meter_pk>\d+)/process/(?P<file_pk>\d+)/$', views.process, name='process'),
    url(r'^meters/(?P<meter_pk>\d+)/graph/$', views.graph_creation, name='graph_creation'),
]

urlpatterns += staticfiles_urlpatterns()
