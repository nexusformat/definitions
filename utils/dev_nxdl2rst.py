#!/usr/bin/env python

'''
Developers: use this code to develop and test nxdl2rst.py
'''

# testing:
# cd /tmp
# mkdir out
# /G/nx-def/utils/nxdl2rst.py /G/nx-def/applications/NXsas.nxdl.xml > nxsas.rst && sphinx-build . out
# then point browser to file:///tmp/out/nxsas.html


import nxdl2rst
import os
import sys


# find the directory of this python file
BASEDIR = os.path.split(os.path.abspath(__file__))[0]


# nxdl = os.path.join(BASEDIR, '..', 'applications', 'NXarchive.nxdl.xml')
# nxdl = os.path.join(BASEDIR, '..', 'applications', 'NXsas.nxdl.xml')
# nxdl = os.path.join(BASEDIR, '..', 'base_classes', 'NXcrystal.nxdl.xml')
# nxdl = os.path.join(BASEDIR, '..', 'base_classes', 'NXobject.nxdl.xml')
# nxdl = os.path.join(BASEDIR, '..', 'contributed_definitions', 'NXarpes.nxdl.xml')
# nxdl = os.path.join(BASEDIR, '..', 'contributed_definitions', 'NXmagnetic_kicker.nxdl.xml')
nxdl = os.path.join(BASEDIR, '..', 'contributed_definitions', 'NXcanSAS.nxdl.xml')

if len(sys.argv) == 1:
    sys.argv.append(nxdl)
elif len(sys.argv) > 1:
    sys.argv[1] = nxdl

nxdl2rst.main()
