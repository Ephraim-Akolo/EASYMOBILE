# EASYMOBILE PYTHON API

## Overview

`easymobile` is a Python package that provides a simple interface for integrating with the EASYMOBILE API, allowing users to purchase airtime, data, cable subscriptions etc. This package is designed to streamline the process of interacting with the EASYMOBILE API and offers methods to handle various operations such as fetching available services, purchasing services, and checking transaction statuses.


## Available Features

- Airtime Operations
- Data Operations
- Cable Operations

## Installation

To install the EasyB2B package, clone this repository and install:

```bash
pip install easymobile
```
or if you wish to install from the git repo.

```bash
# Install from the main branch
pip install git+https://github.com/Ephraim-Akolo/EASYMOBILE.git
```

## Usage

### Initialization

To use the EASYMOBILE package, you need to initialize the classes with your API key. The API key can be provided during initialization or set in the environmental variable `EASYMOBILE_API_KEY`.

### Account Operations

```python
from easymobile import EasyBase

api_key = 'your_api_key'

client = EasyBase(api_key=api_key)

# Get Account Balance
response = client.get_wallet_balance("admin@email.com")
print(response)
```

### Airtime Operations

```python
from easymobile import EasyAirtime, get_easyb2b_reference

api_key = 'your_api_key'

client = EasyAirtime(api_key=api_key)

# Get Networks
networks = client.get_networks()
print(networks)

# Get Airtime Types
airtime_types = client.get_airtime_types(network=1)
print(airtime_types)

# Get Airtime Rates
airtime_rates = client.get_airtime_rates(network=1, airtimeType='VTU')
print(airtime_rates)

# Purchase Airtime
reference = get_easyb2b_reference()  # Generate a unique reference code
response = client.purchase_airtime(reference=reference, network=1, airtimeType='SME', amount='10', phone='08168639124')
print(response)

# Get Transaction Status
status = client.get_transaction_status(ref=reference)
print(status)
```

### Data Operations

```python
from easymobile import EasyData, get_easyb2b_reference

api_key = 'your_api_key'

client = EasyData(api_key=api_key)

# Get Networks
networks = client.get_networks()
print(networks)

# Get Data Types
data_types = client.get_data_types(network=1)
print(data_types)

# Get Data Plans
data_plans = client.get_data_plans(network=1, dataType='SME')
print(data_plans)

# Purchase Data
reference = get_easyb2b_reference()  # Generate a unique reference code
response = client.purchase_data(reference=reference, network=1, dataType='SME', planId='1', phone='08168639113')
print(response)

# Get Transaction Status
status = client.get_transaction_status(ref=reference)
print(status)
```

### Cable Operations

```python
from easymobile import EasyCable, get_easyb2b_reference

api_key = 'your_api_key'

client = EasyCable(api_key=api_key)

# Get Cables
cables = client.get_cables()
print(cables)

# Get Cable Packages
packages = client.get_cable_packages(cable_id=1)
print(packages)

# Validate Smartcard/IUC Number
validation = client.validate_smartcard_iuc_number(cable_id=1, smartcard_no='1234567890')
print(validation)

# Purchase Cable Subscription
reference = get_easyb2b_reference()  # Generate a unique reference code
response = client.purchase_cable(reference=reference, cable_id='1', package_id='1', smartcard_no='1234567890')
print(response)

# Get Transaction Status
status = client.get_transaction_status(ref=reference)
print(status)
```

### Single Client For All Operations

If you require a client object that is capable of accessing all services, you can instantiate the `EasyMobile` class and use `easy_<service name>` to access any service specific methods.

```python
from easymobile import EasyMobile

api_key = 'your_api_key'

client = EasyMobile(api_key=api_key)

# Get Account Balance
response = client.get_wallet_balance("admin@email.com")
print(response)

# Get Networks (Airtime)
networks = client.easy_airtime.get_networks()
print(networks)

# Get Networks (Data)
networks = client.easy_data.get_networks()
print(networks)

# Get Cables
cables = client.easy_cable.get_cables()
print(cables)
```

## Running Tests

To run the tests for the EASYMOBILE package, create and/or activate a Python virtual environment, ensure the current working directory is the root directory, and follow these steps:
```bash
# Install the test dependencies if not already done
pip install -r requirements-test.txt

# Discover and run tests
python -m unittest
```

## Contributing

Contributions are welcome! Please fork the repository and create a pull request to `dev` branch with your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
