#!/usr/bin/env python

'''
Copy all resources for out-of-source documentation build

Since we provide a build for Linux, MacOSX, and Windows,
this tool must be multiplatform.  If only for Linux
(and possibly MacOSX), it might be possible to use a form of::

  cp -a ../base_classes ./
  cp -a ../applications ./
  cp -a ../contributed_definitions ./
  cp -a ../manual ./
  ...

Here, we identify and copy all resources to build.
The target directory is assumed to be the current directory.

'''

# Re-run this code to bring in any changed files (for incremental build)
# Be sure to properly specify the source and target directories.

import os, sys
from local_utilities import replicate


MTIME_TOLERANCE = 0.001   # ignore mtime differences <= 1 ms
ROOT_DIR_EXPECTED_RESOURCES = {
    'files': '''COPYING LGPL.txt Makefile NXDL_VERSION
                nxdl.xsd nxdlTypes.xsd README.md
             '''.split(),
    'subdirs': '''applications base_classes contributed_definitions manual
                 package utils www impatient-guide
               '''.split(),
}
REPLICATED_RESOURCES = '''
    LGPL.txt  Makefile  nxdl.xsd  nxdlTypes.xsd  NXDL_VERSION
    base_classes  applications  contributed_definitions 
    manual  utils impatient-guide
'''.split()


def mtime_size(filename):
    '''get the modification time and size of the given item'''
    file_status = os.stat(filename)
    return file_status.st_mtime, file_status.st_size


def standardize_name(path, resource_name):
    '''always use the absolute path to the filesystem resource'''
    return os.path.abspath(os.path.join(path, resource_name))


def identical(source, target):
    '''compare if the resource is the same on both paths'''
    if not os.path.exists(target):
        return False
    s_mtime, s_size = mtime_size(source)
    t_mtime, t_size = mtime_size(target)
    return abs(s_mtime - t_mtime) <= MTIME_TOLERANCE and s_size == t_size


def get_source_items(resources, source_path):
    '''walk the source_path directories accumulating files to be checked'''
    file_list = []
    path_list = []
    for path in sorted(resources):
        source = standardize_name(source_path, path)
        if os.path.isfile(source):
            file_list.append(source)
        else:
            for root, dirs, files in os.walk(source):
                path_list.append(root)
                file_list = file_list + [os.path.join(root, _) for _ in files]
    return path_list, file_list


def is_definitions_directory(basedir):
    '''test if ``basedir`` is a NeXus definitions directory'''
    # look for the expected files and subdirectories in the root directory
    for item_list in ROOT_DIR_EXPECTED_RESOURCES.values():
        for item in item_list:
            if not os.path.exists(os.path.join(basedir, item)):
                return False
    return True


def qualify_inputs(source_dir, target_path):
    '''raise error if this program cannot continue, based on the inputs'''
    if not os.path.exists(source_dir):
        raise RuntimeError('Cannot find ' + source_dir)

    if not os.path.isdir(source_dir):
        raise RuntimeError('Not a directory: ' + source_dir)

    if not is_definitions_directory(source_dir):
        msg = 'Not a NeXus definitions root directory ' + source_dir
        raise RuntimeError(msg)
    
    if source_dir == target_path:
        msg = 'Source and target directories cannot be the same'
        raise RuntimeError(msg)


def command_args():
    '''get the command-line arguments, handle syntax errors'''
    import argparse
    doc = __doc__.strip().splitlines()[0]
    parser = argparse.ArgumentParser(prog=sys.argv[0], description=doc)
    parser.add_argument('defs_dir',
                        action='store', 
                        help="path to NeXus definitions root directory")
    parser.add_argument('build_dir',
                        action='store', 
                        default=None,
                        nargs='?',
                        help="path to target directory (default: current directory)")
    return parser.parse_args()


def update(source_path, target_path):
    '''
    duplicate directory from source_path to target_path
    
    :param source_path str: source directory (NeXus definitions dir)
    :param target_path str: target directory is specified for build product
    '''
    # TODO: what about file items in target_path that are not in source_path?
    source_path = os.path.abspath(source_path)
    target_path = os.path.abspath(target_path)
    qualify_inputs(source_path, target_path)
    
    paths, files = get_source_items(REPLICATED_RESOURCES, source_path)
    print('source has  %d directories   and   %d files' % (len(paths), len(files)))
    
    # create all the directories / subdirectories
    for source in sorted(paths):
        relative_name = source[len(source_path):].lstrip(os.sep)
        target = standardize_name(target_path, relative_name)
        if not os.path.exists(target):
            print('create directory %s' % target)
            os.mkdir(target, os.stat(source_path).st_mode)
    # check if the files need to be updated
    for source in sorted(files):
        relative_name = source[len(source_path):].lstrip(os.sep)
        target = standardize_name(target_path, relative_name)
        if not identical(source, target):
            print('update file %s' % target)
            replicate(source, target)


def main():
    '''
    standard command-line processing
    
    source directory (NeXus definitions dir) named as command line argument
    target directory is specified (or defaults to present working directory)
    '''
    cli = command_args()
    source_path = os.path.abspath(cli.defs_dir)
    target_path = cli.build_dir or os.path.abspath(os.getcwd())
    update(source_path, target_path)


def __developer_build_setup__():
    '''for use with source-code debugger ONLY'''
    import shutil
    # sys.argv.append('-h')
    os.chdir('../')
    os.chdir('build')
    sys.argv.append('..')


if __name__ == '__main__':
    # __developer_build_setup__()
    main()


# NeXus - Neutron and X-ray Common Data Format
# 
# Copyright (C) 2008-2015 NeXus International Advisory Committee (NIAC)
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
