"""
fillOrBust python package configuration.

Lisa Cicatello <lmcicat@umich.edu>
"""

from setuptools import setup

setup(
    name='fillorbust',
    version='0.1.0',
    packages=['fillorbust'],
    include_package_data=True,
    install_requires=[
        'arrow==0.15.8',
        'bs4==0.0.1',
        'Flask==1.1.1',
        'html5validator==0.3.1',
        'pycodestyle==2.5.0',
        'pydocstyle==4.0.1',
        'pylint==2.3.1',
        'pytest==5.1.2',
        'requests==2.31.0',
        'sh==1.12.14',
        'gunicorn'
    ],
)
