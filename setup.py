# -*- coding: utf-8 -*-
import setuptools


setuptools.setup(
    version='1.2.0',
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
            'M5 = mutable_defaults:MutableDefaultChecker',
        ],
    },
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
