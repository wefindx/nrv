# Copyright (c) 2018 WeFindX Foundation, CLG.
# All Rights Reserved.

from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()


setup(
    name='nrvoc',
    version='0.0.1',
    description='Network Resource Vocabulary.',
    long_description=long_description,
    url='https://gitlab.com/wefindx/nrvoc',
    author='Mindey',
    author_email='mindey@qq.com',
    license='ASK FOR PERMISSIONS',
    packages=find_packages(exclude=['docs', 'tests*']),
    install_requires=[
    ],
    zip_safe=False
)
