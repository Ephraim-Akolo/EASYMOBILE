from easyb2b.base import EasyB2B

class EasyCable(EasyB2B):
    
    def __init__(self, api_key: str = None, timeout=None) -> None:
        super().__init__(api_key, timeout)

    def get_cables(self, cable='all', **kwargs):
        url = f'{self.base_url}/v1/topup/load/cable-types'
        data = {'cables': cable}
        data.update(**kwargs)
        response = self.sess.post(url, json=data, timeout=self.timeout)
        return response.json()
     
    def get_cable_packages(self, cable_id=1, **kwargs):
        url = f'{self.base_url}/v1/topup/load/cable-packages'
        data = {'cableId': str(cable_id)}
        data.update(**kwargs)
        response = self.sess.post(url, json=data, timeout=self.timeout)
        return response.json()
    
    def validate_smartcard_iuc_number(self, cable_id=1, smartcard_no='', **kwargs):
        url = f'{self.base_url}/v1/topup/validate/smartcard-no'
        data = {'cableId': str(cable_id), 'smartCardNo': smartcard_no}
        data.update(**kwargs)
        response = self.sess.post(url, json=data, timeout=self.timeout)
        return response.json()
    
    def purchase_cable(self, reference:str, cable_id:str='1', package_id:str='1', amount_optional:str=None, smartcard_no:str=''):
        url = f'{self.base_url}/v1/topup/cable'
        data = {
            "cableId": str(cable_id),
            "packageId": package_id,
            "smartCardNo": smartcard_no,
            "reference": reference 
        }
        if amount_optional is not None: data["topupAmount"] = amount_optional
        response = self.sess.post(url, json=data, timeout=self.timeout)
        return response.json()
    
    def get_transaction_status(self, ref: str):
        return super().get_transaction_status('cable', ref)


if __name__ == "__main__":
    pass