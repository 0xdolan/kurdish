# -*- coding: utf-8 -*-

from setuptools import setup
from os import path
from io import open


myPath = path.abspath(path.dirname(__file__))
with open(path.join(myPath, 'README.md'), encoding='utf-8') as f:
	README = f.read()

setup(
    name='Kurdish',
    version='1.0.8',
    author='Dolan Hêriş',
    author_email='dolanskurd@mail.com',
    url='https://github.com/dolanskurd',
    description=('Kurdish Language Library for converting characters and digits in Persian, English and Arabic to Kurdish and vice versa.'),
    long_description=README,
    long_description_content_type='text/markdown',
    license='MIT',
    keywords='Kurdish Language Module Library Converter Digits Characters',
    py_modules=['Kurdish'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Documentation',
        'Topic :: Printing',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Editors :: Text Processing',
        'Topic :: Text Processing :: Fonts',
        'Topic :: Text Editors :: Word Processors',
        'Topic :: Utilities',
        'Intended Audience :: Developers',
]
)

