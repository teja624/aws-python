#!/usr/bin/env python

from distutils.core import setup

setup(name='AWS Python',
      version='1.1',
      description='Python AWS Interface',
      author='Tom Hulbert',
      author_email='tom.hulbert@cloudtrek.com.au',
      packages=['sys', 'os', 'menugenerator', 'boto3', 'botocore', 'time'],
     )
