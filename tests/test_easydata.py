import unittest
from easymobile import EasyData, get_easyb2b_reference

class TestEasyData(unittest.TestCase):
    
    def setUp(self):
        self.easy_data = EasyData(api_key='demo')

    def test_get_networks(self):
        response = self.easy_data.get_networks()
        self.assertTrue(response['status'])
        self.assertEqual(response['code'], 200)
        self.assertIn('product', response['data'])

    def test_get_data_types(self):
        response = self.easy_data.get_data_types(network=1)
        self.assertTrue(response['status'])
        self.assertEqual(response['code'], 200)
        self.assertIn('product', response['data'])

    def test_get_data_plans(self):
        response = self.easy_data.get_data_plans(network=1, data_type='SME')
        self.assertTrue(response['status'])
        self.assertEqual(response['code'], 200)
        self.assertIn('product', response['data'])

    def test_purchase_data(self):
        response = self.easy_data.purchase_data(reference=get_easyb2b_reference(), network=1, data_type='SME', plan_id='1', phone='08168639114')
        self.assertTrue(response['status'])
        self.assertEqual(response['code'], 200)

    def test_get_transaction_status(self):
        response = self.easy_data.get_transaction_status(ref='test_ref')
        self.assertTrue(response['status'])
        self.assertEqual(response['code'], 200)

if __name__ == "__main__":
    unittest.main()
