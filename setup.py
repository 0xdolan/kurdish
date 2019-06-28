#!/usr/bin/python3
# -*- coding: utf-8 -*-

from setuptools import setup
from os import path


myPath = path.abspath(path.dirname(__file__))
with open(path.join(myPath, "README.md"), encoding="utf-8") as f:
    README = f.read()

setup(
    name="kurdish",
    version="1.1.4",
    author="Dolan Hêriş",
    author_email="dolanskurd@mail.com",
    url="https://github.com/dolanskurd/kurdish",
    description=(
        "Kurdish Language Library for transliteration from Arabic-based Kurdish to Latin-based Kurdish."
    ),
    long_description=README,
    long_description_content_type="text/markdown",
    license="MIT",
    keywords="kurdish language module library converter digits characters persian farsi arabic latin english transliteration",
    packages=["kurdish"],
    include_package_data=True,
    install_requires=[],
    classifiers=[
        "Topic :: Documentation",
        "Topic :: Printing",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Editors :: Text Processing",
        "Topic :: Text Processing :: Fonts",
        "Topic :: Text Editors :: Word Processors",
        "Topic :: Utilities",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)

