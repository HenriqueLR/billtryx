#encoding: utf-8

'''
More informations you can see documentation 
of the project https://github.com/HenriqueLR/evaluation
'''

from django.shortcuts import render
from core.shots import Dribbble
from django.http import HttpResponseRedirect, HttpResponseNotFound


def list_shots(request):
	try: 
		page = request.GET.get("page")
	except ValueError: 
		page = 1

	try:
		shots = Dribbble()
		shots_list = shots.shots('popular', page=page)
		paginator = shots_list.pop(-1)
	except:
		return HttpResponseNotFound('<h1>Page not found</h1>')

	return render(request,'list_shots.html', {'list_shots':shots_list, 'pagination':paginator})

def view_detail_shots(request, *args, **kwargs):
	try: 
		id_shots = int(kwargs.get('pk'))
	except ValueError: 
		id_shots = 1	

	try:
		shots = Dribbble()
		shots_list = shots.shot(id_shots)
	except:
		return HttpResponseNotFound('<h1>Page not found</h1>')

	return render(request,'detail_shot.html', {'list_shots':shots_list})