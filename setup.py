from setuptools import setup
import re

with open('src/pywildmatch/__init__.py') as fd:
    version = re.search(r'__version__ = \'(.*?)\'', fd.read()).group(1)

setup(name='pywildmatch', version=version)
