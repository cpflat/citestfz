#!/usr/bin/env python

import sys
import os
from setuptools import setup

try:
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst')
except ImportError:
    print('pandoc is not installed.')
    read_md = lambda f: open(f, 'r').read()

setup(name='citestfz',
    version='0.0.1',
    description='',
    long_description=read_md('README.md'),
    author='Satoru Kobayashi',
    author_email='sat@hongo.wide.ad.jp',
    url='https://github.com/cpflat/citestfz/',
    install_requires=['numpy>=1.12.1', 'scipy>=1.0.0'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        ('License :: OSI Approved :: '
         'GNU General Public License v2 or later (GPLv2+)'),
        'Programming Language :: Python :: 3.4.3',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Software Development :: Libraries :: Python Modules'],
    license='GNU General Public License v2 or later (GPLv2+)',
    
    packages=['citestfz'],
    )
