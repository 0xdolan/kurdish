import setuptools

with open('README.txt', 'r', encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
	name='Kurdish',
	version='1.0.3',
	author='Dolan Hêriş',
	author_email='dolanskurd@mail.com',
	url='https://github.com/dolanskurd/Kurdish',
	description=('Kurdish Language Library for converting characters and numbers in Persian, English and also Arabic to Kurdish and vice versa.'),
	long_description = long_description,
	keywords='Kurdish Language Module Library',
	py_modules=['Kurdish'],
	packages=setuptools.find_packages(),
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
	],
)

