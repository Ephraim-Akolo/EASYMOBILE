from .base import EasyB2B


class EasyCable(EasyB2B):
    """
    A class to interact with the EasyB2B API for cable TV-related operations.
    ref: https://b2b.eazymobile.ng/api/developer/v1/documentation/start#item-2-5
    """
    
    def __init__(self, api_key: str = None, timeout=None) -> None:
        """
        Initialize the EasyCable object.
        
        Args:
            api_key (str, optional): The API key for authentication. If not provided, will use the environment variable `EASYB2B_API_KEY`. Set key as "Demo" to use the mocked API.
            timeout (float, optional): Timeout for API requests.
        """
        super().__init__(api_key, timeout)

    def get_cables(self, cable='all', **kwargs):
        """
        Retrieve available cable types.

        Args:
            cable (str, optional): Specify the cable type to retrieve. Default is 'all'. Do not change unless you know what you are doing!
            **kwargs: Additional keyword arguments.

        Returns:
            dict: JSON response from the API.
        """
        url = f'{self.base_url}/v1/topup/load/cable-types'
        data = {'cables': cable}
        data.update(**kwargs)
        response = self.sess.post(url, json=data, timeout=self.timeout)
        return response.json()

    def get_cable_packages(self, cable_id:int, **kwargs):
        """
        Retrieve available packages for a specific cable type.

        Args:
            cable_id (int): Cable ID. Use the `.get_cables` method to fetch available cables and their IDs.
            **kwargs: Additional keyword arguments.

        Returns:
            dict: JSON response from the API.
        """
        url = f'{self.base_url}/v1/topup/load/cable-packages'
        data = {'cableId': str(cable_id)}
        data.update(**kwargs)
        response = self.sess.post(url, json=data, timeout=self.timeout)
        return response.json()

    def validate_smartcard_iuc_number(self, cable_id:int, smartcard_no:str, **kwargs):
        """
        Validate the smartcard/IUC number for a cable service.

        Args:
            cable_id (int): Cable ID. Use the `.get_cables` method to fetch available cables and their IDs.
            smartcard_no (str): Smartcard/IUC number to validate.
            **kwargs: Additional keyword arguments.

        Returns:
            dict: JSON response from the API.
        """
        url = f'{self.base_url}/v1/topup/validate/smartcard-no'
        data = {'cableId': str(cable_id), 'smartCardNo': smartcard_no}
        data.update(**kwargs)
        response = self.sess.post(url, json=data, timeout=self.timeout)
        return response.json()

    def purchase_cable(self, reference:str, cable_id:str, package_id:str, smartcard_no:str, amount_optional:str=None):
        """
        Purchase a cable package for a given smartcard/IUC number.

        Args:
            reference (str): Unique reference for the transaction.
            cable_id (str): Cable ID. Default is '1'.
            package_id (str): Package ID. Default is '1'.
            smartcard_no (str): Smartcard/IUC number.
            amount_optional (str, optional): Optional amount for top-up.

        Returns:
            dict: JSON response from the API.
        """
        url = f'{self.base_url}/v1/topup/cable'
        data = {
            "cableId": str(cable_id),
            "packageId": str(package_id),
            "smartCardNo": smartcard_no,
            "reference": reference 
        }
        if amount_optional is not None:
            data["topupAmount"] = amount_optional
        response = self.sess.post(url, json=data, timeout=self.timeout)
        return response.json()

    def get_transaction_status(self, ref: str):
        """
        Get the status of a specific cable transaction.

        Args:
            ref (str): Reference of the transaction.

        Returns:
            dict: JSON response from the API.
        """
        return super().get_transaction_status('cable', ref)


if __name__ == "__main__":
    pass
