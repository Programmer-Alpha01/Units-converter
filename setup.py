from setuptools import setup

with open("README", 'r') as f:
    long_description = f.read()

setup(
   name='Units-converter', #same as repository name
   version='1.0',
   description='A useful Units converter',
   license="",
   long_description=long_description,
   author='',
   author_email='',
   url="",
   packages=['Units-converter'],  #same as name
   install_requires=[], #external packages as dependencies
   scripts=[
            'scripts/length',
           ]
)