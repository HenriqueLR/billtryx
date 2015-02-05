#encoding: utf-8

'''
More informations you can see documentation 
of the project https://github.com/HenriqueLR/billtryx
'''

from django.shortcuts import render
from core.shots import Dribbble
from django.http import HttpResponseRedirect, HttpResponseNotFound



def view_detail_shots(request, *args, **kwargs):
	pass