from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
	url(r'^$', include('data_viewer.urls')),
	url(r'^data_viewer/', include('data_viewer.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
