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
    if os.path.exists(target):
        shutil.rmtree(target)
    if os.path.exists(source):
        shutil.copytree(source, target)
