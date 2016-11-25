#!/bin/env python

'''
unit testing of NeXus definitions NXDL files and XML Schema
'''

import os
import sys
import unittest
import lxml.etree

# xmllint --noout --schema nxdl.xsd base_classes/NXentry.nxdl.xml 
# base_classes/NXentry.nxdl.xml validates


NXDL_XSD_SCHEMA = 'nxdl.xsd'

class NXDL_Invalid(Exception): pass
class NXDL_Valid(Exception): pass


class TestNXDL(unittest.TestCase):
    
    def setUp(self):
        self.orig_wd = os.getcwd()
        self.basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        os.chdir(self.basedir)
        if not os.path.exists(NXDL_XSD_SCHEMA):
            raise IOError(NXDL_XSD_SCHEMA + " file not found")
        xsd = lxml.etree.parse(NXDL_XSD_SCHEMA)
        self.schema = lxml.etree.XMLSchema(xsd)
    
    def tearDown(self):
        os.chdir(self.orig_wd)
    
    def validate_xml(self, xml_file_name):
        '''
        validate an NXDL XML file against an XML Schema file
    
        :param str xml_file_name: name of XML file
        '''
        xml_tree = lxml.etree.parse(xml_file_name)
        try:
            result = self.schema.assertValid(xml_tree)
            raise NXDL_Valid
        except lxml.etree.DocumentInvalid:
            raise NXDL_Invalid

    def test_all_nxdl_files_against_nxdl_xsd(self):
        for category in ('base_classes applications contributed_definitions'.split() ):
            nxdl_files = [fn for fn in os.listdir(category) if fn.endswith('.nxdl.xml')]
            print sorted(nxdl_files)
            for fn in sorted(nxdl_files):
                self.assertRaises(NXDL_Valid, self.validate_xml, os.path.join(category, fn))


if __name__ == '__main__':
    unittest.main()
