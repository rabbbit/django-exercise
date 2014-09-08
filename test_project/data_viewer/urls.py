from django.conf.urls import patterns, url

from data_viewer import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
	url(r'^csv/$', views.csv_data, name='csv'),
	url(r'^prn/$', views.prn_data, name='prn'),
)
