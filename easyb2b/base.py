import requests, os
from easyb2b.mocked import MockedRequests

API_KEY = os.getenv('EASYB2B_API_KEY')


class EasyB2B(object):
    _mocked = False
    sess = None
    base_url = "https://b2b.eazymobile.ng/api/live"
    timeout = 6.1

    def __init__(self, api_key:str = None, timeout=None) -> None:
        if timeout: self.timeout = timeout
        self.req_session = requests.session()
        self.req_session.headers['Content-Type'] = 'application/json'
        self.req_session.headers['Accept'] = 'application/json'
        self.mocked = False
        if API_KEY:
            self.req_session.headers['Authorization'] = f'Bearer {API_KEY}'
        elif api_key:
            self.req_session.headers['Authorization'] = f'Bearer {api_key}'
        else:
            self.req_session.headers['Authorization'] = f'Bearer Demo'
            self.mocked = True

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
    
    def get_wallet_balance(self, email='example@email.com', **kwargs):
        url = f'{self.base_url}/v1/load/wallet-balance'
        data = {'email': email}
        data.update(**kwargs)
        response = self.sess.post(url, json=data, timeout=self.timeout)
        assert response.status_code == 200
        return response.json()

