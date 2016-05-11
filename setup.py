# -*- coding: utf-8 -*-
import setuptools


setuptools.setup(
    version='1.0.0',
    name='flake-mutable-defaults',
    description='mutable defaults flake8 extension',
    keywords='flake8 mutable arg kwarg',
    author='Matthew Ebeweber',
    author_email='mebeweber@gmail.com',
    url='https://github.com/ebeweber/flake8-mutable-defaults',
    license='MIT',
    install_requires=[
        'flake8',
        'setuptools',
    ],
    entry_points={
        'flake8.extension': [
            'M90 = mutable_defaults:MutableDefaultChecker',
        ],
    },
)
