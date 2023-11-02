import requests, os, random
from datetime import datetime
from .mocked import MockedRequests

API_KEY = os.getenv('EASYB2B_API_KEY')
    

class EasyB2B(object):
    _mocked = False
    sess = None
    base_url = "https://b2b.eazymobile.ng/api/live"
    alphnum = [chr(i) for i in range(48, 58)] + [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
    datetime = datetime.now 

    def __init__(self, api_key:str = None) -> None:
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

    def get_reference(self):
        date = self.datetime()
        code = ''.join(random.sample(self.alphnum, 18))
        return f"{date.year}{date.month:02}{date.day:02}{date.hour:02}{date.minute:02}{code}"
    
    def get_wallet_balance(self, email='example@email.com', **kwargs):
        url = f'{self.base_url}/v1/load/wallet-balance'
        data = {'email': email}
        data.update(**kwargs)
        response = self.sess.post(url, json=data)
        assert response.status_code == 200
        return response.json()


class EasyData(EasyB2B):
    
    def __init__(self, api_key: str = None) -> None:
        super().__init__(api_key) 

    def get_networks(self, networks='all', **kwargs):
        url = f'{self.base_url}/v1/topup/load/networks'
        data = {'networks': networks}
        data.update(**kwargs)
        response = self.sess.post(url, json=data)
        assert response.status_code == 200
        return response.json()
    
    def get_data_types(self, network=1, **kwargs):
        url = f'{self.base_url}/v1/topup/load/data-types'
        data = {'network': str(network)}
        data.update(**kwargs)
        response = self.sess.post(url, json=data)
        assert response.status_code == 200
        return response.json()
    
    def get_data_plans(self, network=1, dataType='SME', **kwargs):
        url = f'{self.base_url}/v1/topup/load/data'
        data = {'network': str(network), 'dataType': dataType}
        data.update(**kwargs)
        response = self.sess.post(url, json=data)
        assert response.status_code == 200
        return response.json()
    
    def purchase_data(self, network=1, dataType='SME', planId='500MB_SME', phone='08168639113'):
        url = f'{self.base_url}/v1/topup/data'
        data = {
            "network": str(network),
            "dataType": dataType,
            "planId": planId,
            "phone": phone,
            "reference": self.get_reference()
        }
        response = self.sess.post(url, json=data)
        assert response.status_code == 200
        return response.json()


if __name__ == "__main__":
    client = EasyData(api_key="live_381d1ce9f6a64ef6a59840849a1b75469m323319")
    print(client.get_data_plans(),sep='\n')