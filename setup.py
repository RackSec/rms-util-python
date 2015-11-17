from setuptools import find_packages, setup

from rmsutil import __version__ as version

setup(
    name='rmsutil',
    version=version,
    description='Common utilities used in RMS projects',
    author='Kurt Griffiths',
    author_email='kurt.griffiths@rackspace.com',
    url='',
    license='Proprietary',
    packages=find_packages(),
    install_requires=[
        'six'
    ],
)
