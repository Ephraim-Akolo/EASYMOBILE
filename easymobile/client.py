from .base import EasyBase


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
    
