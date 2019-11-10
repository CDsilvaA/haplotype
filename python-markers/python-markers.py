#!/usr/bin/env python3

""" python-markers.py: Markers generator using genotype files

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
__author__ = "Thiago Roberto do Prado"
__copyright__ = "Copyright 2017, Thiago Roberto do Prado"
__credits__ = ["Thiago Roberto do Prado", "Cherlynn Daniela da Silva Arce"]

__license__ = "GPL3"
__version__ = "1.0"
__maintainer__ = "Thiago Roberto do Prado"
__email__ = "trprado@outlook.com"

import re
import os
import sys # Packages

path = input('Type the path to files: ') # user digits the directory

# Enter in path directory
os.chdir(path)
# For files in directory generate markers
for lsfile in os.listdir(path): # for every file in the directory
    with open(lsfile, 'r') as fhand: # read the file
        markers = list() # NULL list
        reg = re.compile("MARKERS: (.*)$") # take the information about the markers
        for line in fhand: # for every line
            line = line.rstrip() # separate the line
            m = reg.search(line) # verify if the string match
            if m: # if so
                markers.append(m.group(1)) # store the secod group

        fhand.close() # close the file
        print('Finish to generated list')

    # Generate path in system format
    fpath = ''
    if path[-1] != '/' and sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
        fpath = path + '/' + 'markers/'
        print('Unix based system')
    elif path[-1] != '\\' and sys.platform.startswith('win32'):
        fpath = path + '\\' + 'markers\\'
        print('Microsoft system')
    elif path[-1] == '/' and sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
        fpath = path + 'markers/'
        print('Unix based system')
    elif path[-1] == '\\' and sys.platform.startswith('win32'):
        fpath = path + 'markers\\'
        print('Microsoft system')
    else:
        print('File system unkow to generate path')

    # Create new folder to paste generated markers
    if not os.path.exists('markers'):
        os.mkdir('markers')
        print('folder create: markers')
    print('New folder path is ', fpath)

    # Save markers in file
    with open(fpath + lsfile + '.txt', 'w') as fhand:
        fhand.write('\n'.join(markers))
        fhand.close()
        print('List save in ', fpath+lsfile)
