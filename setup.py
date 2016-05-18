# -*- coding: utf-8 -*-
import setuptools


setuptools.setup(
    version='1.0.3',
    name='flake8-mutable',
    description='mutable defaults flake8 extension',
    keywords='flake8 mutable arg kwarg',
    author='Matthew Ebeweber',
    author_email='mebeweber@gmail.com',
    url='https://github.com/ebeweber/flake8-mutable',
    license='MIT',
    py_modules=['mutable_defaults'],
    zip_safe=False,
    install_requires=[
        'flake8',
    ],
    entry_points={
        'flake8.extension': [
            'M90 = mutable_defaults:MutableDefaultChecker',
        ],
    },
)
