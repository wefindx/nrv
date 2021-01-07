# Copyright (c) 2020 WeFindX Foundation, CLG.
# All Rights Reserved.

from setuptools import find_packages, setup

with open('README.rst', 'r') as f:
    long_description = f.read()


setup(
    name='nrv',
    version='0.1.8',
    description='Network Resource Vocabulary.',
    long_description=long_description,
    url='https://gitlab.com/wefindx/nrv',
    author='Mindey',
    author_email='mindey@qq.com',
    license='MIT',
    packages = find_packages(exclude=['docs', 'tests*']),
    install_requires=['boltons'],
    extras_require = {
        'test': ['coverage', 'pytest', 'pytest-cov'],
    },
    zip_safe=False
)
