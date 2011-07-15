'''
Cryptotrade
---

This module provides wrappers for the Bitcoin trading APIs available from 
MtGox and Tradehill. In the future more trading platforms may be added.
'''

from setuptools import setup

setup(
    name='Cryptotrade',
    version='0.1',
    url='https://github.com/maxcountryman/cryptotrade',
    license='BSD',
    author='Max Countryman',
    author_email='maxc@me.com',
    description='Cryptocurrency trading API wrapper; MtGox and Tradehill',
    long_description=__doc__,
    zip_safe=False,
    platforms='any',
    test_suite='test_cryptotrade'
)

