from django.test import TestCase
from .models import Plane, Passenger
from uuid import UUID

class PlaneTestCase(TestCase):
    def test_plane_create(self):
        request_data = {
                "id": 2341,
                "tank_capacity": 0,
                "consumption": 0
                }
        response = self.client.post('/planes/', data=request_data, content_type='application/json')
        response_data = response.json()
        self.assertEqual(response_data["tank_capacity"], 468200)
        self.assertEqual(response_data["consumption"], 6)


    def test_planes_get(self):
       response = self.client.get('/planes/')
       self.assertNotEqual(response.json(), None)
        
