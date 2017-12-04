#!/usr/bin/python
from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

setup(name='advent_of_code',
      version='1.0',
      description='Solutions to advent of code',
      author='Paul Jones',
      url='https://github.com/pwjones89/advent_of_code',
      license='MIT',
      test_suite='tests',
      )
