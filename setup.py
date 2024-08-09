from setuptools import setup

packages = ["easymobile"]

package_data = {"": ["*"]}

install_requires = ["requests"]

setup_requires = ["setuptools_scm"]

setup_kwargs = {
    "name": "easymobile",
    "use_scm_version": True,  # Automatically uses the version from Git tags
    "description": "EASYMOBILE Python client library",
    "long_description": open("README.md").read(),
    "long_description_content_type": "text/markdown",
    "author": "Ephraim",
    "author_email": "ephraimakolo2017@gmail.com",
    "maintainer": "Akolo Jonah Kutsa",
    "maintainer_email": "ephraimakolo2017@gmail.com",
    "url": "https://github.com/jake-ephraim/EASYMOBILE",
    "packages": packages,
    "package_data": package_data,
    "install_requires": install_requires,
    "setup_requires": setup_requires,
    "python_requires": ">=3.7",
}

setup(**setup_kwargs)
