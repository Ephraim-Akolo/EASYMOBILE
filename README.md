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

### Airtime Operations

```python
from easymobile import EasyAirtime, get_easyb2b_reference

api_key = 'your_api_key'

easy_airtime = EasyAirtime(api_key=api_key)

# Get Networks
networks = easy_airtime.get_networks()
print(networks)

# Get Airtime Types
airtime_types = easy_airtime.get_airtime_types(network=1)
print(airtime_types)

# Get Airtime Rates
airtime_rates = easy_airtime.get_airtime_rates(network=1, airtimeType='VTU')
print(airtime_rates)

# Purchase Airtime
reference = get_easyb2b_reference()  # Generate a unique reference code
response = easy_airtime.purchase_airtime(reference=reference, network=1, airtimeType='SME', amount='10', phone='08168639124')
print(response)

# Get Transaction Status
status = easy_airtime.get_transaction_status(ref=reference)
print(status)
```

### Data Operations

```python
from easymobile import EasyData, get_easyb2b_reference

api_key = 'your_api_key'

easy_data = EasyData(api_key=api_key)

# Get Networks
networks = easy_data.get_networks()
print(networks)

# Get Data Types
data_types = easy_data.get_data_types(network=1)
print(data_types)

# Get Data Plans
data_plans = easy_data.get_data_plans(network=1, dataType='SME')
print(data_plans)

# Purchase Data
reference = get_easyb2b_reference()  # Generate a unique reference code
response = easy_data.purchase_data(reference=reference, network=1, dataType='SME', planId='1', phone='08168639113')
print(response)

# Get Transaction Status
status = easy_data.get_transaction_status(ref=reference)
print(status)
```

### Cable Operations

```python
from easymobile import EasyCable, get_easyb2b_reference

api_key = 'your_api_key'

easy_cable = EasyCable(api_key=api_key)

# Get Cables
cables = easy_cable.get_cables()
print(cables)

# Get Cable Packages
packages = easy_cable.get_cable_packages(cable_id=1)
print(packages)

# Validate Smartcard/IUC Number
validation = easy_cable.validate_smartcard_iuc_number(cable_id=1, smartcard_no='1234567890')
print(validation)

# Purchase Cable Subscription
reference = get_easyb2b_reference()  # Generate a unique reference code
response = easy_cable.purchase_cable(reference=reference, cable_id='1', package_id='1', smartcard_no='1234567890')
print(response)

# Get Transaction Status
status = easy_cable.get_transaction_status(ref=reference)
print(status)
```

## Running Tests

To run the tests for the EASYMOBILE package, create and/or activate a Python virtual environment, ensure the current working directory is the root directory, and follow these steps:
```bash
# Install the test dependencies if not already done
pip install -r test-requirements.txt

# Discover and run tests
python -m unittest
```

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
