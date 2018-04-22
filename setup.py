import os
from setuptools import setup, find_packages


setup(
    name='python-usda',
    version='0.1',
    author='Lucidiot',
    packages=find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    package_data={
        '': ['*.md', 'LICENSE', 'README'],
    },
    install_requires=[
        'enum34>=1.1.3',
        'six>=1.11.0',
        'requests>=2.16.0'
    ],
    extras_require={
        'dev': [
            "pytest",
            "pytest-cov",
            "pytest-pep8"
        ]
    },
    license='GNU General Public License 3',
    description="A fork of pygov focused on USDA nutritional database API",
    long_description=open('README.md').read(),
    keywords="api usda nutrition food",
    url="https://github.com/Lucidiot/python-usda",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6"
    ],
    project_urls={
        "Source Code": "https://github.com/Lucidiot/python-usda",
        "Gitter Chat": "https://gitter.im/BrainshitPseudoScience/Lobby",
    }
)
