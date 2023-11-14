from easyb2b.base import EasyB2B

class EasyAirtime(EasyB2B):
    
    def __init__(self, api_key: str = None, timeout=None) -> None:
        super().__init__(api_key, timeout)

    def get_networks(self, networks='all', **kwargs):
        url = f'{self.base_url}/v1/topup/load/networks'
        data = {'networks': networks}
        data.update(**kwargs)
        response = self.sess.post(url, json=data, timeout=self.timeout)
        assert response.status_code == 200
        return response.json()
    
    def get_airtime_types(self, network=1, **kwargs):
        url = f'{self.base_url}/v1/topup/load/airtime-types'
        data = {'network': str(network)}
        data.update(**kwargs)
        response = self.sess.post(url, json=data, timeout=self.timeout)
        assert response.status_code == 200
        return response.json()
    
    def get_airtime_rates(self, network=1, airtimeType='VTU', **kwargs):
        url = f'{self.base_url}/v1/topup/load/airtime-rate'
        data = {'network': str(network), 'airtimeType': airtimeType}
        data.update(**kwargs)
        response = self.sess.post(url, json=data, timeout=self.timeout)
        assert response.status_code == 200
        return response.json()
    
    def purchase_airtime(self, reference:str, network:str=1, airtimeType:str='SME', amount:str='10', phone:str='08168639113'):
        url = f'{self.base_url}/v1/topup/airtime'
        data = {
            "network": str(network),
            "airtimeType": airtimeType,
            "amount": amount,
            "phone": phone,
            "reference": reference 
        }
        response = self.sess.post(url, json=data, timeout=self.timeout)
        assert response.status_code == 200
        return response.json()
    
    def get_transaction_status(self, ref: str):
        return super().get_transaction_status('airtime', ref)


if __name__ == "__main__":
    pass