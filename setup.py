# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from os.path import dirname, join, realpath

from pkg_resources import parse_requirements
from setuptools import find_packages, setup

_install_requires = parse_requirements(open("requirements.in"))
install_requires = [str(req) for req in _install_requires]

ROOT = realpath(join(dirname(__file__)))

setup(
    name="autorelease",
    version="0.1.0",
    packages=find_packages(),
    author="Mouadh Kaabachi",
    author_email="mouadh.kaabachi@gmail.com",
    description="auto release workflow",
    url="https://github.com",
    long_description=open("README.rst").read(),
    install_requires=install_requires,
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 3 - Alpha",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
    ],
)
