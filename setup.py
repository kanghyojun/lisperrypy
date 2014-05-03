#! -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(name='pylisp',
      version='0.0.1',
      author='Kang Hyojun',
      author_email='hyojun@admire.kr',
      install_requires=[
          'pytest>=2.3.5'
      ],
      packages=find_packages())
