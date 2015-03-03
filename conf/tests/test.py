#encoding: utf-8

'''
More informations you can see documentation 
of the project https://github.com/HenriqueLR/billtryx
'''

from django.test import TestCase
from django.core.urlresolvers import reverse



class ViewShotsTest(TestCase):
    '''
    Testing listing shots.
    '''
    def setUp(self):
        self.url_list_shots = reverse('list_shots')

    def test_view_url(self):
        response = self.client.get(self.url_list_shots)

        self.assertEquals(response.status_code, 200)

        self.assertContains(response, self.url_list_shots)

    def tearDown(self): 
        del self.url_list_shots