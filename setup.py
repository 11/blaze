from setuptools import setup, find_packages


with open('README.md', 'r') as readme:
    long_description = readme.read()


with open('requirements.txt') as f:
    required = f.read().splitlines()
    touchdown_url = required[-1].split('==')[1]
    required[-1] = f'touchdown @ {touchdown_url}'


setup(
    name = 'blaze',
    version='1.0',
    description='site generator for lit-element projects',
    long_description=long_description,
    author='Doug Rudolph',
    url='https://github.com/11/blaze',
    packages=setuptools.find_packages(),
    install_requires=required, 
    
    # creates the `blaze` command on the commandline
    entry_points={
        'console_scripts': [
            'blaze=blaze.__main__:blaze',
        ]
    },
)