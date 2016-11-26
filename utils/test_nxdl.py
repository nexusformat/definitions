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


BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
NXDL_XSD_SCHEMA = 'nxdl.xsd'
NXDL_SCHEMA = lxml.etree.XMLSchema(
    lxml.etree.parse(
        os.path.join(BASE_DIR, NXDL_XSD_SCHEMA)))


class NXDL_Invalid(Exception): pass
class NXDL_Valid(Exception): pass


def isNXDL(fname):
    return fname.endswith('.nxdl.xml')


def get_NXDL_file_list():
    os.chdir(BASE_DIR)
    file_list = []
    for category in ('base_classes applications contributed_definitions'.split() ):
        raw_list = os.listdir(category)
        nxdl_files = [os.path.join(category, fn) for fn in raw_list if isNXDL(fn)]
        file_list += sorted(nxdl_files)
    return file_list


def validate_xml(xml_file_name):
    '''
    validate an NXDL XML file against an XML Schema file

    :param str xml_file_name: name of XML file
    '''
    try:
        xml_tree = lxml.etree.parse(xml_file_name)
    except lxml.etree.XMLSyntaxError as exc:
        msg = xml_file_name + ' : ' + str(exc)
        raise NXDL_Invalid(msg)
    try:
        result = NXDL_SCHEMA.assertValid(xml_tree)
        raise NXDL_Valid
    except lxml.etree.DocumentInvalid as exc:
        msg = xml_file_name + ' : ' + str(exc)
        raise NXDL_Invalid(msg)


class TestMaker(type):
    
    def __new__(cls, clsname, bases, dct):
        # Add a method to the class' __dict__ for every 
        # file name in the NXDL file list.
        for fname in get_NXDL_file_list():
            category, nxdl_name = os.path.split(fname)
            point = nxdl_name.find(".")
            nxdl_name = nxdl_name[:point]
            test_name = 'test_' + category + '_' + nxdl_name
            dct[test_name] = cls.make_test(fname)

        return super(TestMaker, cls).__new__(cls, clsname, bases, dct)

    @staticmethod
    def make_test(nxdl_file_name):
        
        def test_wrap(self):
            # test body for each NXDL file test
            with self.assertRaises(NXDL_Valid):
                validate_xml(nxdl_file_name)
        return test_wrap


# FIXME: only works for python2
class Individual_NXDL_tests(unittest.TestCase):
   __metaclass__ = TestMaker


if __name__ == '__main__':
    unittest.main()
