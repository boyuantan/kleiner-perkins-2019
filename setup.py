#!usr/bin/python
from setuptools import setup, find_packages
setup(
    name = 'Solitaire',
    version = '0.10',
    packages = find_packages(),
    test_suite = 'tests',
    entry_points = {
        'console_scripts': [
            'solitaire = solitaire.__main__:main'
        ]
    }
)