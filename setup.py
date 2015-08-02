#!/usr/bin/env python
import os
from setuptools import setup
from setuptools import find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


setup(
    name = "SourceLib",
    version = "0.0.1",
    description = "Valve Source Dedicated Server Query/RCON/Log protocols",
    author = "Andreas Klauer",
    author_email = "Andreas.Klauer@metamorpher.de",
    url = "https://github.com/kradalby/SourceLib",
    keywords = ["valve", "source", "rcon"],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    long_description='\n\n'.join([read('README.md')]),
    test_suite = 'tests',
    install_requires=[],
    packages=['SourceLib'],
)
