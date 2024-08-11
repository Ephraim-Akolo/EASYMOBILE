import unittest
from easymobile import EasyCable, get_easyb2b_reference

class TestMockedEasyCable(unittest.TestCase):
    
    def setUp(self):
        self.easy_cable = EasyCable(api_key='demo')

    def test_get_cables(self):
        response = self.easy_cable.get_cables()
        self.assertTrue(response['status'])
        self.assertEqual(response['code'], 200)
        self.assertIn('product', response['data'])

    def test_get_cable_packages(self):
        response = self.easy_cable.get_cable_packages(cable_id=3)
        self.assertTrue(response['status'])
        self.assertEqual(response['code'], 200)
        self.assertIn('product', response['data'])

    def test_validate_smartcard_iuc_number(self):
        response = self.easy_cable.validate_smartcard_iuc_number(cable_id=3, smartcard_no='1234567890')
        self.assertTrue(response['status'])
        self.assertEqual(response['code'], 200)
        self.assertIn('validate', response['data'])

    def test_purchase_cable(self):
        response = self.easy_cable.purchase_cable(reference=get_easyb2b_reference(), cable_id='3', package_id='1', smartcard_no='1234567890')
        self.assertTrue(response['status'])
        self.assertEqual(response['code'], 200)

    def test_get_transaction_status(self):
        response = self.easy_cable.get_transaction_status(ref=get_easyb2b_reference())
        self.assertTrue(response['status'])
        self.assertEqual(response['code'], 200)

if __name__ == "__main__":
    unittest.main()
