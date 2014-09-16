#! -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(name='lisperrypy',
      version='0.0.1',
      author='Kang Hyojun',
      author_email='hyojun@admire.kr',
      tests_require=[
          'pytest>=2.3.5', 'tox>=1.7.2'
      ],
      packages=find_packages())
