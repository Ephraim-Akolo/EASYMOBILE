
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

    def __call__(self, url, data=None, json=None, **kwargs):
        assert isinstance(json, dict)
        assert 'Content-Type' in kwargs['headers'].keys()
        assert 'Accept' in kwargs['headers'].keys()
        assert 'Authorization' in kwargs['headers'].keys()
        assert kwargs['headers']['Content-Type'] == 'application/json'
        assert kwargs['headers']['Accept'] == 'application/json'
        assert 'Bearer ' in kwargs['headers']['Authorization']
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


