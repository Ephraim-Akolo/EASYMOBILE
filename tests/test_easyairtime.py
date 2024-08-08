import unittest
from unittest.mock import patch
from easymobile import EasyAirtime, get_easyb2b_reference

class TestMockedEasyAirtime(unittest.TestCase):
    
    def setUp(self):
        self.easy_airtime = EasyAirtime(api_key='demo')

    def test_get_networks(self):
        response = self.easy_airtime.get_networks()
        self.assertTrue(response['status'], response)
        self.assertIn('product', response['data'])

    def test_get_airtime_types(self):
        response = self.easy_airtime.get_airtime_types(network=1)
        self.assertTrue(response['status'])
        self.assertIn('product', response['data'])

    def test_get_airtime_rates(self):
        response = self.easy_airtime.get_airtime_rates(network=1, airtime_type='VTU')
        self.assertTrue(response['status'])
        # self.assertIn('rate', response['data']['product'])

    def test_purchase_airtime(self):
        response = self.easy_airtime.purchase_airtime(reference=get_easyb2b_reference(), network=1, airtime_type='SME', amount='10', phone='08168639114')
        self.assertTrue(response['status'])
        self.assertEqual(response['data']['message'], 'SUCCESSFUL')

    # def test_get_transaction_status(self):
    #     response = self.easy_airtime.get_transaction_status(ref=get_easyb2b_reference())
    #     print(response)
    #     self.assertTrue(response['status'], response)
        # self.assertEqual(response['data']['transaction'], 'completed')

if __name__ == "__main__":
    unittest.main()
