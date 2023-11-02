import requests, os, random
from datetime import datetime
from .mocked import MockedRequests

API_KEY = os.getenv('EASYB2B_API_KEY')
    

class EasyB2B(object):
    base_url = "https://b2b.eazymobile.ng/api/live"
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }
    alphnum = [chr(i) for i in range(48, 58)] + [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
    datetime = datetime.now 
    post = requests.post

    _mocked = False

    def __init__(self, api_key:str = None) -> None:
        if API_KEY:
            self.headers['Authorization'] = f'Bearer {API_KEY}'
        elif api_key:
            self.headers['Authorization'] = f'Bearer {api_key}'
        else:
            self.headers['Authorization'] = f'Bearer Demo'
            self.mocked = True

    @property
    def mocked(self):
        return self._mocked
    
    @mocked.setter
    def mocked(self, val):
        if not isinstance(val, bool):
            raise ValueError("property mocked must be a boolean value!")
        if val:
            self.post = MockedRequests()
        else:
            self.post = requests.post
        self._mocked = val

    def get_reference(self):
        date = self.datetime()
        code = ''.join(random.sample(self.alphnum, 18))
        return f"{date.year}{date.month:02}{date.day:02}{date.hour:02}{date.minute:02}{code}"
    
    def get_wallet_balance(self, email='example@email.com', **kwargs):
        url = f'{self.base_url}/v1/load/wallet-balance'
        data = {'email': email}
        data.update(**kwargs)
        response = self.post(url=url, headers=self.headers, json=data)
        assert response.status_code == 200
        return response.json()


class EasyData(EasyB2B):
    
    def __init__(self, api_key: str = None) -> None:
        super().__init__(api_key) 

    def get_networks(self, networks='all', **kwargs):
        url = f'{self.base_url}/v1/topup/load/networks'
        data = {'networks': networks}
        data.update(**kwargs)
        response = self.post(url=url, headers=self.headers, json=data)
        assert response.status_code == 200
        return response.json()
    
    def get_data_types(self, network=1, **kwargs):
        url = f'{self.base_url}/v1/topup/load/data-types'
        data = {'network': str(network)}
        data.update(**kwargs)
        response = self.post(url=url, headers=self.headers, json=data)
        assert response.status_code == 200
        return response.json()
    
    def get_data_plans(self, network=1, dataType='SME', **kwargs):
        url = f'{self.base_url}/v1/topup/load/data'
        data = {'network': str(network), 'dataType': dataType}
        data.update(**kwargs)
        response = self.post(url=url, headers=self.headers, json=data)
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
        response = self.post(url=url, headers=self.headers, json=data)
        assert response.status_code == 200
        return response.json()


if __name__ == "__main__":
    client = EasyData()
    print(client.get_networks(), client.get_data_types(), client.get_data_plans(), client.get_wallet_balance(), client.purchase_data(), sep='\n')