#!/usr/bin/env python

# Coded for both python2 and python3.

'''
Common code for NeXus definitions Python tools

======================  ==================================
tool                    description
======================  ==================================
:meth:`printf`          wrapper for Python 2.x and 3.x
:meth:`mtime`           return file modification time
:meth:`replicate_tree`  copy directory stack or file
======================  ==================================

'''

from __future__ import print_function
import os, sys, re
import shutil



def printf(str, *args):
    '''wrapper for Python 2.x and 3.x'''
    print(str % args, end='')


def mtime(file_name):
    '''return file modification time'''
    return os.stat(file_name)[stat.ST_MTIME]


def replicate(source, target):
    '''
    for directories or files: copy ``source`` to ``target``, replaces ``target``
    
    :param str source: path to source resource
    :param str target: path to target location
    '''
    if os.path.isfile(source):
        shutil.copy2(source, target)
    elif os.path.isdir(source):
        replicate_tree(source, target)
    else:
        msg = 'Do not know how to copy (skipped): ' + source
        raise RuntimeWarning(msg)


def replicate_tree(source, target):
    '''
    for directories: copy ``source`` to ``target``, replaces ``target``
    
    :param str source: path to source resource (a directory)
    :param str target: path to target location (a directory)
    '''
    if os.path.exists(source):
        if os.path.exists(target):
            shutil.rmtree(target, ignore_errors=True)
        shutil.copytree(source, target)
    else:
        raise RuntimeError('Directory not found: ' + source)


# NeXus - Neutron and X-ray Common Data Format
# 
# Copyright (C) 2008-2021 NeXus International Advisory Committee (NIAC)
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
