#encoding: utf-8

'''
More informations you can see documentation 
of the project https://github.com/HenriqueLR/billtryx
'''

import time, urllib, urllib2
from pagination import Pagination
import json



API_URL = 'http://api.dribbble.com/' 


_TRACK_CALLS = False
_calls = []

def _api(url, id, pagination=None):
	if _TRACK_CALLS:
		_calls.append(time.time())

	if pagination:
		query = '?' + urllib.urlencode(zip(('page', 'per_page'), pagination))
	else:
		query = ''

	u = urllib2.urlopen(API_URL + (url % id) + query)
	return json.loads(u.read())

class Dribbble(object):
	def __init__(self, track_calls=False):

		global _TRACK_CALLS
		if track_calls:
			_TRACK_CALLS = True

	def shot(self, shotid):
		return Shot(_api('shots/%d', shotid))

	def shots(self, typ='everyone', page=1, per_page=15):

		data = _api('shots/%s', typ, (page, per_page))

		shots = [Shot(sd) for sd in data['shots']]
		shots.append(Pagination(data['page'],data['per_page'],data['total']))
		return shots

	def calls(self):
		return _calls

class Shot(object):

	def __init__(self, data):
		for k, v in data.items():
			if k != u'player':
				setattr(self, k, v)
		self.player = Player(data[u'player'])

class Player(object):

	def __init__(self, data, username=None):
		for k, v in data.items():
			setattr(self, k, v)

		self.username = self.url.strip('/').rsplit('/', 1)[-1]