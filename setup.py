#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
]

test_requirements = [
    'pytest',
    'pdbpp',
]

setup(
    name='chess_configurations',
    version='0.1.0',
    description="Finds all unique configurations of a set of normal chess pieces on a chess boa",
    long_description=readme + '\n\n' + history,
    author="Leonardo Lazzaro",
    author_email='llazzaro@dc.uba.ar',
    url='https://github.com/llazzaro/chess_configurations',
    packages=[
        'chess_configurations',
    ],
    dependency_links=[
    ],
    package_dir={'chess_configurations':
                 'chess_configurations'},
    entry_points={
        'console_scripts': [
            'chess_configurations=chess_configurations.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='chess_configurations',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
