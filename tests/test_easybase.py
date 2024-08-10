import unittest
from easymobile import EasyBase


class TestMockedEasyBase(unittest.TestCase):
    
    def setUp(self):
        self.easy_base = EasyBase(api_key='demo')

    def test_get_wallet_balance(self):
        response = self.easy_base.get_wallet_balance('example@email.com')
        self.assertTrue(response['status'], response)
        self.assertEqual(response['code'], 200)
        self.assertIn('product', response['data'])
