from easyb2b import exceptions
from easyb2b.base import EasyB2B

class EasyAirtime(EasyB2B):
    """
    A class to interact with the EasyB2B API for airtime-related operations.
    ref: https://b2b.eazymobile.ng/api/developer/v1/documentation/start#item-2-4
    """
    
    def __init__(self, api_key: str = None, timeout=None) -> None:
        """
        Initialize the EasyAirtime object.
        
        Args:
            api_key (str, optional): The API key for authentication. If not provided, will use the environment variable `EASYB2B_API_KEY`.
            timeout (float, optional): Timeout for the requests. Default is 45.1 seconds.
        """
        super().__init__(api_key, timeout)

    def get_networks(self, networks:str='all', **kwargs):
        """
        Query all the networks for airtime top-up.

        Args:
            networks (str, optional): Specify the network to retrieve. Default is 'all'. Do not change unless you know what you are doing!
            **kwargs: Additional keyword arguments.

        Returns:
            dict: JSON response from the API.
        """
        url = f'{self.base_url}/v1/topup/load/networks'
        data = {'networks': networks}
        data.update(**kwargs)
        response = self.sess.post(url, json=data, timeout=self.timeout)
        try:
            response = self.sess.post(url, json=data, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except exceptions.RequestException as e:
            return {'error': str(e)}

    def get_airtime_types(self, network:int, **kwargs):
        """
        Retrieve available airtime types for a specific network.

        Args:
            network (int): Network ID. Use the `.get_networks` method to fetch available networks and their IDs.
            **kwargs: Additional keyword arguments.

        Returns:
            dict: JSON response from the API.
        """
        url = f'{self.base_url}/v1/topup/load/airtime-types'
        data = {'network': str(network)}
        data.update(**kwargs)
        try:
            response = self.sess.post(url, json=data, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except exceptions.RequestException as e:
            return {'error': str(e)}

    def get_airtime_rates(self, network:int, airtime_type:str, **kwargs):
        """
        Retrieve airtime rates for a specific network and airtime type.

        Args:
            network (int): Network ID. Use the `.get_networks` method to fetch available networks and their IDs.
            airtime_type (str): Type of airtime. Use the `.get_airtime_types` method to fetch available network types and their names.
            **kwargs: Additional keyword arguments.

        Returns:
            dict: JSON response from the API.
        """
        url = f'{self.base_url}/v1/topup/load/airtime-rate'
        data = {'network': str(network), 'airtimeType': airtime_type}
        data.update(**kwargs)
        try:
            response = self.sess.post(url, json=data, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except exceptions.RequestException as e:
            return {'error': str(e)}

    def purchase_airtime(self, reference: str, network:int, airtime_type:str, amount:int, phone:str):
        """
        Purchase airtime for a given phone number.

        Args:
            reference (str): Unique reference for the transaction. (see https://b2b.eazymobile.ng/api/developer/v1/documentation/start#item-2-14 ).
            network (int): Network ID. Use the `.get_networks` method to fetch available networks and their IDs.
            airtime_type (str): Type of airtime. Use the `.get_airtime_types` method to fetch available network types and their names.
            amount (int|str): Amount of airtime to top-up.
            phone (str): Phone number to receive the airtime.

        Returns:
            dict: JSON response from the API.
        """
        url = f'{self.base_url}/v1/topup/airtime'
        data = {
            "network": str(network),
            "airtimeType": airtime_type,
            "amount": str(amount),
            "phone": phone,
            "reference": reference 
        }
        try:
            response = self.sess.post(url, json=data, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except exceptions.RequestException as e:
            return {'error': str(e)}

    def get_transaction_status(self, ref: str):
        """
        Get the status of a specific airtime transaction.

        Args:
            ref (str): Reference of the transaction you generated and supplied.

        Returns:
            dict: JSON response from the API.
        """
        return super().get_transaction_status('airtime', ref)


if __name__ == "__main__":
    pass
