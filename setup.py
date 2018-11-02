#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import Enum
from setuptools import setup, find_packages


version = "0.1.3"


packages = find_packages(
    where="src",
    include=["uuidadapter"]
)


package_dir = {'': 'src'}


# package_data = {}


install_requirements = [
    "construct>=2.9"
]


setup_requirements = [
    "bumpversion>=0.5"
]


test_requirements = [
    "pytest>=3.9",
    "pytest-cov",
    "pytest-pep8",
    "pytest-mypy"
]


# extra_requirements = {}


class Status(Enum):
    PLAN = (1, "Planning")
    PRE = (2, "Pre-Alpha")
    ALPHA = (3, "Alpha")
    BETA = (4, "Beta")
    STABLE = (5, "Production/Stable")

    @property
    def classifier(self):
        return 'Development Status :: {:d} - {:s}'.format(*self.value)


classifiers = [
    Status.STABLE.classifier,
    "Intended Audience :: Developers"
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7"
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]


setup(
    name="construct-uuid",
    version=version,
    packages=packages,
    package_dir=package_dir,
    url="https://github.com/phuntimes/construct-uuid",
    license="MIT License",
    author="Sean McVeigh",
    author_email="smcveigh@gmail.com",
    description="UUID adapter for Construct",
    classifiers=classifiers,
    install_requires=install_requirements,
    # setup_requires=setup_requirements
    tests_require=test_requirements,
    # extras_require=extra_requirements
)
