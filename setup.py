# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in daileemart/__init__.py
from daileemart import __version__ as version

setup(
	name='daileemart',
	version=version,
	description='Customizations for Daileemart',
	author='TEAMPRO',
	author_email='abdulla.pi@groupteampro.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
