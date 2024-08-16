import unittest
from easymobile import EasyMobile

class TestMockedEasyMobile(unittest.TestCase):
    
    def setUp(self):
        self.client = EasyMobile(api_key='demo')

    def test_get_airtime_networks(self):
        response = self.client.easy_airtime.get_networks()
        self.assertTrue(response['status'], response)
        self.assertEqual(response['code'], 200)
        self.assertIn('product', response['data'])

    def test_get_data_networks(self):
        response = self.client.easy_data.get_networks()
        self.assertTrue(response['status'], response)
        self.assertEqual(response['code'], 200)
        self.assertIn('product', response['data'])
    
    def test_get_cable_networks(self):
        response = self.client.easy_cable.get_cables()
        self.assertTrue(response['status'], response)
        self.assertEqual(response['code'], 200)
        self.assertIn('product', response['data'])