import importlib

from setuptools import setup

spec = importlib.util.spec_from_file_location("version", "easyb2b/version.py")
version_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(version_module)

packages = ["easyb2b"]

package_data = {"": ["*"]}

install_requires = [
    "requests",
]

setup_kwargs = {
    "name": "easyb2b",
    "version": version_module.VERSION,
    "description": "EASYMOBILE Python client library",
    "long_description": open("README.md").read(),
    "long_description_content_type": "text/markdown",
    "author": "Ephraim",
    "author_email": "ephraimakolo2017@gmail.com",
    "maintainer": None,
    "maintainer_email": None,
    "url": "https://github.com/jake-ephraim/EASYMOBILE",
    "packages": packages,
    "package_data": package_data,
    "install_requires": install_requires,
    "python_requires": ">=3.7",
}


setup(**setup_kwargs)
