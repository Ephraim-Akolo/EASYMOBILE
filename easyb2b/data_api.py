from easyb2b.base import EasyB2B

class EasyData(EasyB2B):
    
    def __init__(self, api_key: str = None, timeout=None) -> None:
        super().__init__(api_key, timeout)

    def get_networks(self, networks='all', **kwargs):
        url = f'{self.base_url}/v1/topup/load/networks'
        data = {'networks': networks}
        data.update(**kwargs)
        response = self.sess.post(url, json=data, timeout=self.timeout)
        assert response.status_code == 200
        return response.json()
    
    def get_data_types(self, network=1, **kwargs):
        url = f'{self.base_url}/v1/topup/load/data-types'
        data = {'network': str(network)}
        data.update(**kwargs)
        response = self.sess.post(url, json=data, timeout=self.timeout)
        assert response.status_code == 200
        return response.json()
    
    def get_data_plans(self, network=1, dataType='SME', **kwargs):
        url = f'{self.base_url}/v1/topup/load/data'
        data = {'network': str(network), 'dataType': dataType}
        data.update(**kwargs)
        response = self.sess.post(url, json=data, timeout=self.timeout)
        assert response.status_code == 200
        return response.json()
    
    def purchase_data(self, reference:str, network=1, dataType='SME', planId='1', phone='08168639113'):
        url = f'{self.base_url}/v1/topup/data'
        data = {
            "network": str(network),
            "dataType": dataType,
            "planId": planId,
            "phone": phone,
            "reference": reference 
        }
        response = self.sess.post(url, json=data, timeout=self.timeout)
        assert response.status_code == 200
        return response.json()
    
    def get_transaction_status(self, ref: str):
        return super().get_transaction_status('data', ref)


if __name__ == "__main__":
    pass