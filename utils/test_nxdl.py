#!/bin/env python

"""
unit testing of NeXus definitions NXDL files and XML Schema
"""

import os
import sys
import unittest
import lxml.etree

# xmllint --noout --schema nxdl.xsd base_classes/NXentry.nxdl.xml
# base_classes/NXentry.nxdl.xml validates


BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
NXDL_XSD_SCHEMA = "nxdl.xsd"
NXDL_SCHEMA = lxml.etree.XMLSchema(
    lxml.etree.parse(os.path.join(BASE_DIR, NXDL_XSD_SCHEMA))
)

NXDL_CATEGORY_NAMES = "base_classes applications contributed_definitions".split()


class NXDL_Invalid(Exception):
    pass


class NXDL_Valid(Exception):
    pass


def isNXDL(fname):
    return fname.endswith(".nxdl.xml")


def get_NXDL_file_list():
    os.chdir(BASE_DIR)
    file_list = []
    for category in NXDL_CATEGORY_NAMES:
        raw_list = os.listdir(category)
        nxdl_files = [os.path.join(category, fn) for fn in raw_list if isNXDL(fn)]
        file_list += sorted(nxdl_files)
    return file_list


def validate_xml(xml_file_name):
    """
    validate an NXDL XML file against an XML Schema file

    :param str xml_file_name: name of XML file
    """
    try:
        xml_tree = lxml.etree.parse(xml_file_name)
    except lxml.etree.XMLSyntaxError as exc:
        msg = xml_file_name + " : " + str(exc)
        raise NXDL_Invalid(msg)
    try:
        result = NXDL_SCHEMA.assertValid(xml_tree)
        # there is no assertNotRaises so raise this when successful
        raise NXDL_Valid
    except lxml.etree.DocumentInvalid as exc:
        msg = xml_file_name + " : " + str(exc)
        raise NXDL_Invalid(msg)


class TestMaker(type):
    def __new__(cls, clsname, bases, dct):
        # Add a method to the class' __dict__ for every
        # file name in the NXDL file list.
        cat_number_dict = {c: str(i + 1) for i, c in enumerate(NXDL_CATEGORY_NAMES)}
        for fname in get_NXDL_file_list():
            category, nxdl_name = os.path.split(fname)
            category_number = cat_number_dict[category]
            point = nxdl_name.find(".")
            nxdl_name = nxdl_name[:point]
            test_name = "test"
            # since these will be sorted, get the categories in the desired order
            test_name += "__" + str(category_number)
            test_name += "__" + category
            test_name += "__" + nxdl_name
            dct[test_name] = cls.make_test(fname)

        return super(TestMaker, cls).__new__(cls, clsname, bases, dct)

    @staticmethod
    def make_test(nxdl_file_name):
        def test_wrap(self):
            # test body for each NXDL file test
            with self.assertRaises(NXDL_Valid):
                validate_xml(nxdl_file_name)
            self.assertRaises(NXDL_Valid, validate_xml, nxdl_file_name)

        return test_wrap


class Individual_NXDL_Tests(unittest.TestCase, metaclass=TestMaker):
    """
    run all tests created in TestMaker() class, called by suite()
    """


def suite(*args, **kw):
    """gather all the tests together in a suite, called by run()"""
    test_suite = unittest.TestSuite()
    test_suite.addTests(unittest.makeSuite(Individual_NXDL_Tests))
    return test_suite


def run():
    """run all the unit tests"""
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())


if __name__ == "__main__":
    run()
