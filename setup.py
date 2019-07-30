#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from setuptools import find_packages, setup

import app

CLASSIFIERS = [
    "Development Status :: 3 - Alpha",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3.7",
    "Operating System :: OS Independent",
    "Topic :: System :: Networking",
    "Topic :: Software Development",
    "Topic :: Software Development :: Libraries",
    "Environment :: Console",
    "Intended Audience :: Developers",
]


def _get_requires(option):
    with open(f"requirements/{option}.txt") as f:
        return f.read().splitlines()


setup(


    name="mt-driver",
    description="MT driver",
    version=app.__version__,

    platforms=CLASSIFIERS,
    install_requires=_get_requires("prod"),
    extras_require={"tests": _get_requires("tests"), "dev": _get_requires("dev")},
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    test_suite="",
)
