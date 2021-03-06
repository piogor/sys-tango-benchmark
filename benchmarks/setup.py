#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2018  Jan Kotanski <jankotan@gmail.com> / S2Innovation
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation in  version 3
# of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA  02110-1301, USA.
#
# Distributed under the terms of the GPL license.
# See LICENSE.txt for more info.

import os
import sys
from setuptools import setup
# from distutils.core import Command
# from sphinx.setup_command import BuildDoc
from benchmarks.release import name, version

setup_dir = os.path.dirname(os.path.abspath(__file__))

# make sure we use latest info from local code
sys.path.insert(0, setup_dir)

# readme_filename = os.path.join(setup_dir, 'README.rst')
# with open(readme_filename) as file:
#     long_description = file.read()

release_filename = os.path.join(setup_dir, 'benchmarks', 'release.py')
exec(open(release_filename).read())

pack = ['benchmarks']

#: metadata for distutils
SETUPDATA = dict(
    name=name,
    version=version,
    description='Benchmarks for counting attribute, '
    'command and pipe calls',
    packages=pack,
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'pipebenchmark = benchmarks.pipebenchmark:main',
            'readbenchmark = benchmarks.readbenchmark:main',
            'writebenchmark = benchmarks.writebenchmark:main',
            'eventbenchmark = benchmarks.eventbenchmark:main',
            'cmdbenchmark = benchmarks.cmdbenchmark:main',
        ]},
    author='Jan Kotanski, Piotr Goryl',
    author_email='jankotan at gmail.com, piotr.goryl at s2innovation.com',
    license='GPL',
    # long_description=long_description,
    url='www.tango-controls.org',
    platforms="All Platforms",
    # cmdclass={'test': TestCommand, 'build_sphinx': BuildDoc},
)


def main():
    """ the main function """
    setup(**SETUPDATA)


if __name__ == '__main__':
    main()
