"""Setup aws-pylib."""
from setuptools import setup, find_packages

setup(
    name="iwaiwa",
    version="0.1.0",
    description="",
    packages=find_packages(where='src'),
    package_dir={'': 'src'}
)
