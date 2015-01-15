#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This file is part of **python-openzwave** project http://code.google.com/p/python-openzwave.
    :platform: Unix, Windows, MacOS X

.. moduleauthor:: bibi21000 aka Sébastien GALLET <bibi21000@gmail.com>

License : GPL(v3)

**python-openzwave** is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

**python-openzwave** is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with python-openzwave. If not, see http://www.gnu.org/licenses.

"""
from os import name as os_name
from distutils.core import setup
from Cython.Distutils import extension
from Cython.Distutils import build_ext
from platform import system as platform_system
import glob
import os
import sys

ext_modules = [
  extension.Extension(
    "libopenzwave", ["lib/libopenzwave.pyx"],
    libraries=['udev', 'stdc++', 'openzwave'],
    language="c++",
    extra_objects=['/usr/local/lib/libopenzwave.so'],
    include_dirs=['/usr/local/include/openzwave', '/usr/local/include/openzwave/value_classes', '/usr/local/include/openzwave/platform'])
]

setup(
  name = 'python-openzwave-lib',
  author='Sébastien GALLET aka bibi2100 <bibi21000@gmail.com>',
  author_email='bibi21000@gmail.com',
  version = '0.2.6',
  url='http://code.google.com/p/python-openzwave',
  cmdclass = {'build_ext': build_ext},
  ext_modules = ext_modules,
  package_dir = {'libopenzwave' : 'lib'},
  #The following line install config drectory in share/python-openzwave
  data_files = [],
  packages = ['libopenzwave']
)
