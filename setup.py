#!/usr/bin/env python

# This file is part of python-libmilter.
# 
# python-libmilter is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# python-libmilter is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with python-libmilter.  If not, see <http://www.gnu.org/licenses/>.

from distutils.core import setup

setup(name='python-libmilter' ,
    version='1.0.1' ,
    author='Jay Deiman' ,
    author_email='admin@splitstreams.com' ,
    url='http://stuffivelearned.org/doku.php?id=programming:python:python-libmilter' ,
    description='A pure python implementation of libmilter' ,
    py_modules=['libmilter'] ,
    long_description='Full documentation can be found at: '
        'http://stuffivelearned.org/doku.php?id=programming:python:python-libmilter' ,
    classifiers=[
        'Development Status :: 4 - Beta' ,
        'Environment :: No Input/Output (Daemon)' ,
        'Intended Audience :: System Administrators' ,
        'Intended Audience :: Information Technology' ,
        'License :: OSI Approved :: GNU General Public License (GPL)' ,
        'Natural Language :: English' ,
        'Operating System :: POSIX' ,
        'Programming Language :: Python' ,
        'Topic :: System :: Systems Administration' ,
        'Topic :: System' ,
    ]
)
