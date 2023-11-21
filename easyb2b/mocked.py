
class MockedRequests(object):

    base_url = "https://b2b.eazymobile.ng/api"

    urls = (
        # Airtime and Data
        ((f'{base_url}/live/v1/load/wallet-balance', f"{base_url}/test/v1/load/wallet-balance"), 
         {"status": True, "code": 200, "data": {"product": {"wallet": "82318.60"}}}
         ),
        ((f'{base_url}/live/v1/topup/load/networks', f'{base_url}/test/v1/topup/load/networks'), 
         {'status': True, 'code': 200, 'data': {'product': [{'network': 'MTN', 'networkId': 1}, {'network': 'AIRTEL', 'networkId': 2}, {'network': 'GLO', 'networkId': 3}, {'network': '9MOBILE', 'networkId': 4}]}}
         ),
        ((f'{base_url}/live/v1/topup/load/airtime-types', f'{base_url}test/v1/topup/load/airtime-types'), 
         {'status': True, 'code': 200, 'data': {'product': [{'network': 'MTN', 'networkId': 1, 'name': 'VTU'}, {'network': 'MTN', 'networkId': 1, 'name': 'SNS'}, {'network': 'MTN', 'networkId': 1, 'name': 'AWOOF4U'}, {'network': 'MTN', 'networkId': 1, 'name': 'GARABASA'}]}}
         ),
        ((f'{base_url}/live/v1/topup/load/data-types', f'{base_url}test/v1/topup/load/data-types'), 
         {'status': True, 'code': 200, 'data': {'product': [{'network': 'MTN', 'networkId': 1, 'name': 'SME'}, {'network': 'MTN', 'networkId': 1, 'name': 'CORPORATE GIFTING'}, {'network': 'MTN', 'networkId': 1, 'name': 'DIRECT GIFTING'}, {'network': 'MTN', 'networkId': 1, 'name': 'NORMAL GIFTING'}]}}
         ),
        ((f'{base_url}/live/v1/topup/load/airtime-rate', f'{base_url}test/v1/topup/load/airtime-rate'), 
         {'status': True, 'code': 200, 'data': {'product': {'rate': '97%'}}}
         ),
        ((f'{base_url}/live/v1/topup/load/data', f'{base_url}test/v1/topup/load/data'), 
         {'status': True, 'code': 200, 'data': {'product': [{'network': 'MTN', 'planName': '500MB [SME] - 30 DAYS', 'planId': '1', 'price': '140', 'status': 'AVAILABLE'}, {'network': 'MTN', 'planName': '1GB [SME] - 30 DAYS', 'planId': '2', 'price': '240', 'status': 'AVAILABLE'}, {'network': 'MTN', 'planName': '2GB [SME] - 30 DAYS', 'planId': '3', 'price': '480', 'status': 'AVAILABLE'}, {'network': 'MTN', 'planName': '3GB [SME] - 30 DAYS', 'planId': '4', 'price': '720', 'status': 'AVAILABLE'}, {'network': 'MTN', 'planName': '5GB [SME] - 30 DAYS', 'planId': '5', 'price': '1200', 'status': 'AVAILABLE'}, {'network': 'MTN', 'planName': '10GB [SME] - 30 DAYS', 'planId': '6', 'price': '2400', 'status': 'AVAILABLE'}]}}
         ),
        ((f"{base_url}/live/v1/topup/airtime", f"{base_url}/test/v1/topup/airtime"), 
         {'status': True, 'code': 200, 'data': {'message': 'SUCCESSFUL', 'reference': 'EZM20230811025911PIY3BD11'}, 'time': '2023-08-11 02:59:13'}
         ),
        ((f"{base_url}/live/v1/topup/data", f"{base_url}/test/v1/topup/data"), 
         {'status': True, 'code': 200, 'data': {'message': 'Dear Customer, You have successfully shared 500MB Data to 2348168639113. Your SME data balance is 26648.71GB expires 08/02/2024. Thankyou', 'reference': 'EZM20230311083236YLURDN36'}, 'time': '2023-03-11 08:32:39'}
         ),

        # Cables
        ((f"{base_url}/live/v1/topup/load/cable-types", f"{base_url}/test/v1/topup/load/cable-types"), 
         {"status": True, "code": 200, "data": {"product": [{"cable": "DSTV", "cableId": 1},{ "cable": "STARTIMES", "cableId": 2},{ "cable": "GOTV", "cableId": 3}]}}
         ),
        ((f"{base_url}/live/v1/topup/load/cable-packages", f"{base_url}/test/v1/topup/load/cable-packages"),
         {"status": True, "code": 200, "data": {"product": [{"packageId": "1", "cable": "GOTV", "cableId": 3, "name": "GOTV SMALLIE", "price": "1100"}, { "packageId": "2", "cable": "GOTV", "cableId": 3, "name": "GOTV JINJA", "price": "2250"},]}}
        ),
        ((f"{base_url}/live/v1/topup/validate/smartcard-no", f"{base_url}/test/v1/topup/validate/smartcard-no"),
         {"status": True,"code": 200,"data": {"validate": {"customerName": "A***DE DA****", "dueDate": "June 14th, 2023", "currentPackage": "GOTV JOLLI N2,800", "renewalAmount": 3280, "status": "SUSPENDED"}}}
        ),
        ((f"{base_url}/live/v1/topup/cable", f"{base_url}/test/v1/topup/cable"),
         {"status": True, "code": 200, "data": {"message": "Success! Your cable purchase was successful!", "reference": "WPY20232806015819AUQQZ719" }, "time": "2023-28-06 01:58:21"}
        ),

        )


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
            return ResponseJson(obj[-1])
        return ResponseJson({"details": f"{url} not found!"}, status_code=404)

class ResponseJson:
    
    def __init__(self, json, status_code=200) -> None:
        self.data = json
        self.status_code = status_code
    
    def json(self):
        return self.data


