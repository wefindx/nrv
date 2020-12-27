# Copyright (c) 2020 WeFindX Foundation, CLG.
# All Rights Reserved.

from setuptools import find_packages, setup

with open('README.rst', 'r') as f:
    long_description = f.read()


setup(
    name='nrv',
    version='0.0.2',
    description='Network Resource Vocabulary.',
    long_description=long_description,
    url='https://gitlab.com/wefindx/nrv',
    author='Mindey',
    author_email='mindey@qq.com',
    license='MIT',
    zip_safe=False
)
