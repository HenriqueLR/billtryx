from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^billtryx/', include(admin.site.urls)),
    url(r'^$', 'seek.views.list_shots', name='list_shots'),
    url(r'^detail_shots/(?P<pk>\d+)$', 'seek.views.view_detail_shots', name='view_detail_shots'),
)
