#!/usr/bin/env python

'''
update the copyright date in all NeXus text files

This is the bash command to find all matching lines::

  grep -iR copyright | grep -i "(c)" | grep -i nexus

See copyright text at bottom of this file for example.
'''

import os, sys
import mimetypes
import local_utilities
from build_preparation import ROOT_DIR_EXPECTED_RESOURCES
import datetime

YEAR = datetime.datetime.now().year
LEFT_SIDE_TEXT_MATCH = 'Copyright (C) '
RIGHT_SIDE_TEXT_MATCH = ' NeXus International Advisory Committee (NIAC)'


def update(filename):
    '''update the copyright year in the file'''
    def position(line, key):
        pos = line.find(key)
        if pos >= 0:
            if line.find('NIAC') >= 0:
                return pos
        return None
        
    if not os.path.exists(filename):
        return
    changes = []
    buf = open(filename).readlines()
    for number, line in enumerate(buf):
        pos = position(line, LEFT_SIDE_TEXT_MATCH)
        if pos is None:
            continue    # no match

        pos += len(LEFT_SIDE_TEXT_MATCH)
        text_l = line[:pos]

        text = line[pos:]
        pos = text.find(RIGHT_SIDE_TEXT_MATCH)
        text_r = text[pos:]

        try:
            years = list(map(int, text[:pos].split('-')))
            if len(years) in (1, 2):
                if len(years) == 1:
                    years.append(YEAR)
                elif len(years) == 2:
                    years[1] = YEAR
                line_new = text_l + '-'.join(map(str, years)) + text_r
                changes.append(list((number, line_new)))
        except Exception as _exc:
            print(number, filename, str(_exc))
    for number, line in changes:
        buf[number] = line
    if len(changes) > 0:
        print('Update: ', filename)
        fp = open(filename, 'w')
        fp.writelines(buf)
        fp.close()


def find_source_files(path):
    '''walk the source_path directories accumulating files to be checked'''
    file_list = []
    for root, dirs, files in os.walk(path):
        if root.find('/.git') < 0 or root.find('/kits') < 0:
            file_list = file_list + [os.path.join(root, _) for _ in files]
    return file_list


def sift_file_list(file_list):
    '''remove known non-text files and paths'''
    new_list = []
    acceptable_mime_types = '''
        application/xml
        application/x-msdos-program
        application/xslt+xml
    '''.strip().split()
    ignore_extensions = '''
    .dia .vsdx .h5 .nx .hdf5 .hdf .nx5 .pyc
    '''.strip().split()
    for fn in file_list:
        _fn = os.path.split(fn)[-1]
        mime = mimetypes.guess_type(fn)[0]
        if fn.find('/.git') >= 0:
            continue
        if fn.find('/.settings') >= 0:
            continue
        if fn.find('/kits') >= 0:
            continue
        if fn.find('/build') >= 0:
            continue
        if os.path.splitext(fn)[-1] in ignore_extensions:
            continue
        if mime is None or mime.startswith('text/') or mime in acceptable_mime_types:
            new_list.append(fn)
    return new_list


def is_definitions_directory(basedir):
    '''test if ``basedir`` is a NeXus definitions directory'''
    # look for the expected files and subdirectories in the root directory
    for item_list in ROOT_DIR_EXPECTED_RESOURCES.values():
        for item in item_list:
            if not os.path.exists(os.path.join(basedir, item)):
                return False
    return True


def qualify_inputs(root_dir):
    '''raise error if this program cannot continue, based on the inputs'''
    if not os.path.exists(root_dir):
        raise RuntimeError('Cannot find ' + root_dir)

    if not os.path.isdir(root_dir):
        raise RuntimeError('Not a directory: ' + root_dir)

    if not is_definitions_directory(root_dir):
        msg = 'Not a NeXus definitions root directory ' + root_dir
        raise RuntimeError(msg)


def command_args():
    '''get the command-line arguments, handle syntax errors'''
    import argparse
    doc = __doc__.strip().splitlines()[0]
    parser = argparse.ArgumentParser(prog=sys.argv[0], description=doc)
    parser.add_argument('defs_dir',
                        action='store', 
                        help="NeXus definitions root directory")
    return parser.parse_args()


def main():
    '''
    standard command-line processing
    
    source directory (NeXus definitions dir) named as command line argument
    target directory is specified (or defaults to present working directory)
    '''
    cli = command_args()
    root_dir = os.path.abspath(cli.defs_dir)
    qualify_inputs(root_dir)
    
    file_list = sift_file_list(find_source_files(root_dir))
    for fn in file_list:
        update(fn)


def __developer_build_setup__():
    '''for use with source-code debugger ONLY'''
    import shutil
    # sys.argv.append('-h')
    sys.argv.append('..')


if __name__ == '__main__':
    #__developer_build_setup__()
    main()


# NeXus - Neutron and X-ray Common Data Format
# 
# Copyright (C) 2008-2022 NeXus International Advisory Committee (NIAC)
# 
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 3 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# For further information, see http://www.nexusformat.org
