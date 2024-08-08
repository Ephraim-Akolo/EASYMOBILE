import requests
import os
from . import exceptions
from .mocked import MockedRequests

API_KEY = os.getenv('EASYMOBILE_API_KEY')

class EasyBase:
    """
    A class to interact with the EasyB2B API.
    
    Attributes:
        api_key (str): The API key for authentication.
        timeout (float): The timeout for API requests.
    """
    _mocked = False
    sess = None
    base_url = "https://b2b.eazymobile.ng/api/live"
    timeout = 45.1

    def __init__(self, api_key: str = None, timeout: float = None) -> None:
        """
        Initialize the EasyB2B object.
        """
        if timeout:
            self.timeout = timeout

        self.req_session = requests.session()
        self.req_session.headers['Content-Type'] = 'application/json'
        self.req_session.headers['Accept'] = 'application/json'

        if api_key:
            self.req_session.headers['Authorization'] = f'Bearer {api_key}'
            self.mocked = True if api_key.lower() == 'demo' else False
        elif API_KEY:
            self.req_session.headers['Authorization'] =  f'Bearer {API_KEY}'
            self.mocked = True if API_KEY.lower() == 'demo' else False
        else:
            raise ValueError("Invalid or No API key provided!")

    @property
    def mocked(self):
        return self._mocked

    @mocked.setter
    def mocked(self, val):
        if not isinstance(val, bool):
            raise ValueError("property mocked must be a boolean value!")
        if val:
            self.sess = MockedRequests(session=self.req_session)
        else:
            self.sess = self.req_session
        self._mocked = val

    def get_wallet_balance(self, email, **kwargs):
        """
        Get the wallet balance for a given email.

        Args:
            email (str): The email to get the wallet balance for.

        Returns:
            dict: The response from the API as a JSON dictionary.
        """
        url = f'{self.base_url}/v1/load/wallet-balance'
        data = {'email': email}
        data.update(**kwargs)
        try:
            response = self.sess.post(url, json=data, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except exceptions.RequestException as e:
            return {'error': str(e)}

    def get_transaction_status(self, name: str, ref: str):
        """
        Get the transaction status for a given transaction reference.

        Args:
            name (str): The name/type associated with the transaction.
            ref (str): The reference of the transaction.

        Returns:
            dict: The response from the API as a JSON dictionary.
        """
        url = f'{self.base_url}/v1/transaction/status/{name}'
        data = {"reference": ref}
        try:
            response = self.sess.post(url, json=data, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except exceptions.RequestException as e:
            return {'error': str(e)}
