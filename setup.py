#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.md').read()

setup(
    name='pyliczba',
    version='1.0.0',
    description=("Pyliczba is a Python utility module for converting numerical"
                 "values to Polish text, useful in printing invoices etc."),
    long_description=readme,
    author="Rafal Dowgird",
    author_email='',
    url='https://github.com/dowgrid/pyliczba',
    packages=[
        'pyliczba',
    ],
    package_dir={'pyliczba':
                 'pyliczba'},
    include_package_data=True,
    install_requires=[],
    license="BSD",
    zip_safe=False,
    keywords='pyliczba',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    test_suite='tests',
    tests_require=[]
)
