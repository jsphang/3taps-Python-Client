import os
import sys
import warnings

from setuptools import setup, find_packages

if sys.version_info < (2, 6):
  raise SystemExit("Python 2.6 or later is required.")

if sys.version_info > (3, 0):
	warnings.warn("Untested on Python 3; some features may be broken.", RuntimeWarning)


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
	return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
	name = "3taps-Python-Client",
	version = "1.0",
	description = ("3taps Python API Wrappers"),
	long_description=read('README'),

	author = "Erik Westra",
	author_email = "ewestra@gmail.com",
	url = "https://github.com/3taps/3taps-Python-Client",
	license = "BSD",

	test_suite="runTests",

	classifiers=[
		"Development Status :: 5 - Production/Stable",
		"Environment :: Console",
		"Intended Audience :: Developers",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
		"Programming Language :: Python",
		"Programming Language :: Python :: 2.6",
		"Programming Language :: Python :: 2.7",
		"Topic :: Software Development :: Libraries :: Python Modules"
	],

	#packages=['threetaps',],
	packages = find_packages(exclude=['examples', 'tests']),

	install_requires = [
		'simplejson < 2.0',
	],
)
