
class MockedRequests:
    """
    A class to mock API responses for testing purposes.
    
    Attributes:
        session (requests.Session): The session with pre-configured headers.
    """
    base_url = "https://b2b.eazymobile.ng/api"
    urls = [
        # Airtime and Data
        (f'{base_url}/live/v1/load/wallet-balance', f"{base_url}/test/v1/load/wallet-balance", {"status": True, "code": 200, "data": {"product": {"wallet": "82318.60"}}}),
        (f'{base_url}/live/v1/topup/load/networks', f'{base_url}/test/v1/topup/load/networks', {'status': True, 'code': 200, 'data': {'product': [{'network': 'MTN', 'networkId': 1}, {'network': 'AIRTEL', 'networkId': 2}, {'network': 'GLO', 'networkId': 3}, {'network': '9MOBILE', 'networkId': 4}]}}),
        (f'{base_url}/live/v1/topup/load/airtime-types', f'{base_url}/test/v1/topup/load/airtime-types', {'status': True, 'code': 200, 'data': {'product': [{'network': 'MTN', 'networkId': 1, 'name': 'VTU'}, {'network': 'MTN', 'networkId': 1, 'name': 'SNS'}, {'network': 'MTN', 'networkId': 1, 'name': 'AWOOF4U'}, {'network': 'MTN', 'networkId': 1, 'name': 'GARABASA'}]}}),
        (f'{base_url}/live/v1/topup/load/data-types', f'{base_url}/test/v1/topup/load/data-types', {'status': True, 'code': 200, 'data': {'product': [{'network': 'MTN', 'networkId': 1, 'name': 'SME'}, {'network': 'MTN', 'networkId': 1, 'name': 'CORPORATE GIFTING'}, {'network': 'MTN', 'networkId': 1, 'name': 'DIRECT GIFTING'}, {'network': 'MTN', 'networkId': 1, 'name': 'NORMAL GIFTING'}]}}),
        (f'{base_url}/live/v1/topup/load/airtime-rate', f'{base_url}/test/v1/topup/load/airtime-rate', {'status': True, 'code': 200, 'data': {'product': {'rate': '97%'}}}),
        (f'{base_url}/live/v1/topup/load/data', f'{base_url}/test/v1/topup/load/data', {'status': True, 'code': 200, 'data': {'product': [{'network': 'MTN', 'planName': '500MB [SME] - 30 DAYS', 'planId': '1', 'price': '140', 'status': 'AVAILABLE'}, {'network': 'MTN', 'planName': '1GB [SME] - 30 DAYS', 'planId': '2', 'price': '240', 'status': 'AVAILABLE'}, {'network': 'MTN', 'planName': '2GB [SME] - 30 DAYS', 'planId': '3', 'price': '480', 'status': 'AVAILABLE'}, {'network': 'MTN', 'planName': '3GB [SME] - 30 DAYS', 'planId': '4', 'price': '720', 'status': 'AVAILABLE'}, {'network': 'MTN', 'planName': '5GB [SME] - 30 DAYS', 'planId': '5', 'price': '1200', 'status': 'AVAILABLE'}, {'network': 'MTN', 'planName': '10GB [SME] - 30 DAYS', 'planId': '6', 'price': '2400', 'status': 'AVAILABLE'}]}}),
        (f"{base_url}/live/v1/topup/airtime", f"{base_url}/test/v1/topup/airtime", {'status': True, 'code': 200, 'data': {'message': 'SUCCESSFUL', 'reference': 'EZM20230811025911PIY3BD11'}, 'time': '2023-08-11 02:59:13'}),
        (f"{base_url}/live/v1/topup/data", f"{base_url}/test/v1/topup/data", {'status': True, 'code': 200, 'data': {'message': 'Dear Customer, You have successfully shared 500MB Data to 2348168639113. Your SME data balance is 26648.71GB expires 08/02/2024. Thankyou', 'reference': 'EZM20230311083236YLURDN36'}, 'time': '2023-03-11 08:32:39'}),

        # Cables
        (f"{base_url}/live/v1/topup/load/cable-types", f"{base_url}/test/v1/topup/load/cable-types", {"status": True, "code": 200, "data": {"product": [{"cable": "DSTV", "cableId": 1},{ "cable": "STARTIMES", "cableId": 2},{ "cable": "GOTV", "cableId": 3}]}}),
        (f"{base_url}/live/v1/topup/load/cable-packages", f"{base_url}/test/v1/topup/load/cable-packages", {"status": True, "code": 200, "data": {"product": [{"packageId": "1", "cable": "GOTV", "cableId": 3, "name": "GOTV SMALLIE", "price": "1100"}, { "packageId": "2", "cable": "GOTV", "cableId": 3, "name": "GOTV JINJA", "price": "2250"},]}}),
        (f"{base_url}/live/v1/topup/validate/smartcard-no", f"{base_url}/test/v1/topup/validate/smartcard-no", {"status": True,"code": 200,"data": {"validate": {"customerName": "A***DE DA****", "dueDate": "June 14th, 2023", "currentPackage": "GOTV JOLLI N2,800", "renewalAmount": 3280, "status": "SUSPENDED"}}}),
        (f"{base_url}/live/v1/topup/cable", f"{base_url}/test/v1/topup/cable", {"status": True, "code": 200, "data": {"message": "Success! Your cable purchase was successful!", "reference": "WPY20232806015819AUQQZ719" }, "time": "2023-28-06 01:58:21"}),
    ]

    def __init__(self, session=None) -> None:
        """
        Initialize the MockedRequests object.

        Args:
            session (requests.Session, optional): The session with pre-configured headers.
        """
        self.headers = session.headers if session else {}

    def post(self, url: str, data=None, json=None, **kwargs):
        """
        Mock the POST request to return predefined responses.

        Args:
            url (str): The URL for the POST request.
            data (dict, optional): The data to send in the body of the POST request.
            json (dict, optional): The JSON data to send in the body of the POST request.

        Returns:
            ResponseJson: The mocked response object.
        """
        if 'headers' in kwargs:
            self.headers.update(kwargs['headers'])
        
        # Assertions to ensure the request format is correct
        assert isinstance(json, dict), "The 'json' parameter must be a dictionary."
        assert 'Content-Type' in self.headers and self.headers['Content-Type'] == 'application/json'
        assert 'Accept' in self.headers and self.headers['Accept'] == 'application/json'
        assert 'Authorization' in self.headers and 'Bearer ' in self.headers['Authorization']

        # Find the matching URL and return the predefined response
        for live_url, test_url, response in self.urls:
            if url == live_url or url == test_url:
                return ResponseJson(response)
        
        return ResponseJson({"details": f"{url} not found!"}, status_code=404)

class ResponseJson:
    """
    A class to mock the response object.

    Attributes:
        json (dict): The JSON response data.
        status_code (int): The HTTP status code of the response.
    """
    
    def __init__(self, json: dict, status_code: int = 200) -> None:
        self.data = json
        self.status_code = status_code
    
    def json(self):
        """
        Return the JSON data of the response.

        Returns:
            dict: The JSON response data.
        """
        return self.data
