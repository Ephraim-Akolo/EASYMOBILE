from . import EasyBase, EasyAirtime, EasyData, EasyCable


class EasyMobile(EasyBase):
    """
    A class to interact with the Easymobile API.
    ref: https://b2b.eazymobile.ng/api/developer/v1/documentation/start#
    """

    def __init__(self, api_key: str = None, timeout=None) -> None:
        """
        Initialize the EasyAirtime object.
        
        Args:
            api_key (str, optional): The API key for authentication. If not provided, will use the environment variable `EASYB2B_API_KEY`. Set key as "Demo" to use the mocked API.
            timeout (float, optional): Timeout for the requests. Default is 45.1 seconds.
        """
        super().__init__(api_key, timeout)
        self._api_key = api_key


    @property
    def easy_airtime(self):
        try:
            return self._easy_airtime_
        except AttributeError:
            self._easy_airtime_ = EasyAirtime(self._api_key, self.timeout)
        return self._easy_airtime_
    
    @property
    def easy_data(self):
        try:
            return self._easy_data_
        except AttributeError:
            self._easy_data_ = EasyData(self._api_key, self.timeout)
        return self._easy_data_
    
    @property
    def easy_cable(self):
        try:
            return self._easy_cable_
        except AttributeError:
            self._easy_cable_ = EasyCable(self._api_key, self.timeout)
        return self._easy_cable_
        
