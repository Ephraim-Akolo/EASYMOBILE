from easyb2b import exceptions
from easyb2b.base import EasyB2B


class EasyData(EasyB2B):
    """
    A class to interact with the EasyB2B API for data-related operations.
    ref: https://b2b.eazymobile.ng/api/developer/v1/documentation/start#item-2-3
    """
    
    def __init__(self, api_key:str=None, timeout=None) -> None:
        """
        Initialize the EasyData object.
        
        Args:
            api_key (str, optional): The API key for authentication. If not provided, will use the environment variable `EASYB2B_API_KEY`. Set key as "Demo" to use the mocked API..
            timeout (float, optional): Timeout for the requests. Default is 45.1 seconds.
        """
        super().__init__(api_key, timeout)

    def get_networks(self, networks='all', **kwargs):
        """
        Retrieve available networks for data top-up.

        Args:
            networks (str, optional): Specify the network to retrieve. Default is 'all'. Do not change unless you know what you are doing!
            **kwargs: Additional keyword arguments.

        Returns:
            dict: JSON response from the API.
        """
        url = f'{self.base_url}/v1/topup/load/networks'
        data = {'networks': networks}
        data.update(**kwargs)
        try:
            response = self.sess.post(url, json=data, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except exceptions.RequestException as e:
            return {'error': str(e)}


    def get_data_types(self, network:int, **kwargs):
        """
        Retrieve available data types for a specific network.

        Args:
            network (int): Network ID. Use the `.get_networks` method to fetch available networks and their IDs.
            **kwargs: Additional keyword arguments.

        Returns:
            dict: JSON response from the API.
        """
        url = f'{self.base_url}/v1/topup/load/data-types'
        data = {'network': str(network)}
        data.update(**kwargs)
        try:
            response = self.sess.post(url, json=data, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except exceptions.RequestException as e:
            return {'error': str(e)}


    def get_data_plans(self, network:int, data_type:str, **kwargs):
        """
        Retrieve data plans for a specific network and data type.

        Args:
            network (int): Network ID. Use the `.get_networks` method to fetch available networks and their IDs.
            data_type (str): Type of data. Use the `.get_data_types` method to fetch available data types.
            **kwargs: Additional keyword arguments.

        Returns:
            dict: JSON response from the API.
        """
        url = f'{self.base_url}/v1/topup/load/data'
        data = {'network': str(network), 'dataType': data_type}
        data.update(**kwargs)
        try:
            response = self.sess.post(url, json=data, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except exceptions.RequestException as e:
            return {'error': str(e)}


    def purchase_data(self, reference:str, network:int, data_type:str, plan_id:str, phone:str):
        """
        Purchase data for a given phone number.

        Args:
            reference (str): Unique reference for the transaction. (see https://b2b.eazymobile.ng/api/developer/v1/documentation/start#item-2-14 ).
            network (int): Network ID. Default is 1. Use the `.get_networks` method to fetch available networks and their IDs.
            data_type (str): Type of data. Use the `.get_data_types` method to fetch available data types.
            plan_id (str): ID of the data plan. Use the `.get_data_plans` method to fetch available data plans.
            phone (str): Phone number to receive the data.

        Returns:
            dict: JSON response from the API.
        """
        url = f'{self.base_url}/v1/topup/data'
        data = {
            "network": str(network),
            "dataType": data_type,
            "planId": str(plan_id),
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
        Get the status of a specific data transaction.

        Args:
            ref (str): Reference of the transaction.

        Returns:
            dict: JSON response from the API.
        """
        return super().get_transaction_status('data', ref)


if __name__ == "__main__":
    pass
