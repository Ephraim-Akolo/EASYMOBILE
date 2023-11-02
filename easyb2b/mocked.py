
class MockedRequests(object):

    base_url = "https://b2b.eazymobile.ng/api"

    urls = (
        ((f'{base_url}/live/v1/load/wallet-balance', f"{base_url}/test/v1/load/wallet-balance"), "get_wallet_balance_mocked_response"),
        ((f'{base_url}/live/v1/topup/load/networks', f'{base_url}/test/v1/topup/load/networks'), "get_networks_data_mocked_response"),
        ((f'{base_url}/live/v1/topup/load/data-types', f'{base_url}test/v1/topup/load/data-types'), "get_data_types_mocked_response"),
        ((f'{base_url}/live/v1/topup/load/data', f'{base_url}test/v1/topup/load/data'), "get_data_plans_mocked_response"),
        ((f"{base_url}/live/v1/topup/data", f"{base_url}/test/v1/topup/data"), "purchase_data_mocked_response"),
        )
    
    get_wallet_balance_mocked_response = {
            "status": True,
            "code": 200,
            "data": {
                "product": {
                    "wallet": "82318.60"
                }
            }
        }
    
    get_networks_data_mocked_response = {
            "status": True,
            "code": 200,
            "data": {
                "product": [
                    {
                        "network": "MTN",
                        "networkId": 1
                    },
                    {
                        "network": "AIRTEL",
                        "networkId": 2
                    },
                    {
                        "network": "GLO",
                        "networkId": 3
                    },
                    {
                        "network": "9MOBILE",
                        "networkId": 4
                    }
                ]
            }
        }
    
    get_data_types_mocked_response = {
            "status": True,
            "code": 200,
            "data": {
                "product": [
                    {
                        "network": "MTN",
                        "networkId": 1,
                        "name": "SME"
                    },
                    {
                        "network": "MTN",
                        "networkId": 1,
                        "name": "CORPORATE GIFTING"
                    },
                    {
                        "network": "MTN",
                        "networkId": 1,
                        "name": "DIRECT GIFTING"
                    },
                    {
                        "network": "MTN",
                        "networkId": 1,
                        "name": "NORMAL GIFTING"
                    }
                ]
            }
        }
    
    get_data_plans_mocked_response = {
            "status": True,
            "code": 200,
            "data": {
                "product": [
                    {
                        "network": "MTN",
                        "networkId": 1,
                        "name": "SME"
                    },
                    {
                        "network": "MTN",
                        "networkId": 1,
                        "name": "CORPORATE GIFTING"
                    },
                    {
                        "network": "MTN",
                        "networkId": 1,
                        "name": "DIRECT GIFTING"
                    },
                    {
                        "network": "MTN",
                        "networkId": 1,
                        "name": "NORMAL GIFTING"
                    }
                ]
            }
        }

    purchase_data_mocked_response = {
            "status": True,
            "code": 200,
            "data": {
                "message": "Dear Customer, You have successfully shared 500MB Data to 23481663****2. 9961.07 31\\/08\\/2023. Thankyou",
                "reference": "WPY20232806094208VBLWM308"
            },
            "time": "2023-28-06 09:42:16"
        }
    
    def __init__(self, session=None) -> None:
        if session:
            self.headers:dict = session.headers

    def post(self, url, data=None, json=None, **kwargs):
        assert isinstance(json, dict)
        if 'headers' in kwargs:
            self.headers.update(**kwargs["headers"])
        assert 'Content-Type' in self.headers.keys()
        assert 'Accept' in self.headers.keys()
        assert 'Authorization' in self.headers.keys()
        assert self.headers['Content-Type'] == 'application/json'
        assert self.headers['Accept'] == 'application/json'
        assert 'Bearer ' in self.headers['Authorization']
        for obj in self.urls:
            if url not in  obj[0]:
                continue
            func = obj[1]
            return ResponseJson(getattr(self, func))
        

class ResponseJson:
    
    def __init__(self, json, status_code=200) -> None:
        self.data = json
        self.status_code = status_code
    
    def json(self):
        return self.data


