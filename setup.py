# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='scikit-build',
    version='0.17.5',
    description='Improved build system generator for Python C/C++/Fortran/Cython extensions',
    author='The scikit-build team',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Typing :: Typed',
    ],
    install_requires=[
        'distro',
        'packaging',
        'setuptools>=42.0.0',
        'tomli; python_version < "3.11"',
        'typing-extensions>=3.7; python_version < "3.8"',
        'wheel>=0.32.0',
    ],
    extras_require={
        'cov': [
            'coverage[toml]>=4.2',
            'pytest-cov>=2.7.1',
        ],
        'docs': [
            'pygments',
            'sphinx-issues',
            'sphinx-rtd-theme>=1.0',
            'sphinx>=4',
            'sphinxcontrib-moderncmakedomain>=3.19',
        ],
        'doctest': [
            'ubelt>=0.8.2',
            'xdoctest>=0.10.0',
        ],
        'test': [
            'build>=0.7',
            'cython>=0.25.1',
            'importlib-metadata; python_version < "3.8"',
            'pytest-mock>=1.10.4',
            'pytest-virtualenv>=1.2.5',
            'pytest>=6.0.0',
            'requests',
            'virtualenv',
        ],
    },
    packages=[
        'skbuild',
        'skbuild._compat',
        'skbuild.command',
        'skbuild.platform_specifics',
        'skbuild.utils',
    ],
)
