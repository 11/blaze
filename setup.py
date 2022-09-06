from setuptools import setup, find_packages

with open('README.md', 'r') as readme:
    long_description = readme.read()

setup(
    name = 'blaze',
    version='1.0',
    description='site generator for lit-element projects',
    long_description=long_description,
    author='Doug Rudolph',
    url='https://github.com/11/blaze',
    packages=setuptools.find_packages()
)