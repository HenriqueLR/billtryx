#encoding: utf-8

'''
More informations you can see documentation 
of the project https://github.com/HenriqueLR/billtryx
'''

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView



urlpatterns = patterns('',

    url(r'^billtryx/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name='list_shots.html'), name='list_shots'),
)
