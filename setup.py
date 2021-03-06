#!/usr/bin/env python

from distutils.core import setup

setup(name='hpswitch',
        version='0.1',
        description="A library for interacting with HP Networking switches",
        packages=['hpswitch', ],
        url='https://github.com/leonhandreke/hpswitch',
        license="MIT License",
        install_requires=['pysnmp>=4.2.3', 'pysnmp-mibs>=0.1.4']
        )
