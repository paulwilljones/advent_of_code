#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'fn',# TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='day1',
    version='0.1.0',
    description="Day 1 solution for Advent of Code 2",
    long_description=readme + '\n\n' + history,
    author="Paul Jones",
    author_email='paulwilljones@gmail.com',
    url='https://github.com/paulwilljones/day1',
    packages=[
        'day1',
    ],
    package_dir={'day1':
                 'day1'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='day1',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
