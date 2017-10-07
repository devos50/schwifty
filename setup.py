from setuptools import setup, find_packages

setup(
    name='Schwifty',
    version='0.1',
    description='A description.',
    packages=find_packages(),
    package_data={'schwifty': ['*']},
    include_package_data=True,
    install_requires=[],
)
