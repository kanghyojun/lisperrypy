#! -*- coding: utf-8 -*-
from setuptools import setup, find_packages


tests_require = [
    'pytest>=2.3.5', 'tox>=1.7.2'
]

docs_require = [
    'sphinx>=1.2'
]

setup(name='lisperrypy',
      version='0.0.1',
      author='Kang Hyojun',
      author_email='hyojun@admire.kr',
      tests_require=tests_require,
      extras_require={
          'docs': docs_require,
          'tests': tests_require
      },
      packages=find_packages(),
      entry_points={
          'console_scripts': 'lisperrypy = lisperrypy.script:main'
      })
