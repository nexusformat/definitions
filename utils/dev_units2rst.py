#!/usr/bin/env python

'''
Developers: use this code to develop and test nxdl2rst.py
'''

import sys
from units2rst import worker


sys.argv.append("../nxdlTypes.xsd")
worker('anyUnitsAttr')
