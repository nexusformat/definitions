#!/bin/env python

'''
unit testing: NXDL to RST for documentation
'''

import os
import sys
import unittest
import lxml.etree
from io import StringIO

import nxdl2rst


class Capture_stdout(list):
    '''
    capture all printed output (to stdout) into list
    
    # http://stackoverflow.com/questions/16571150/how-to-capture-stdout-output-from-a-python-function-call
    '''
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout


class Issue_524_Clarify_Optional_or_Required(unittest.TestCase):
    '''
    make it obvious what is required and what is optional
    
    **field**: (optional or required) NX_TYPE
    '''
        
    def test_base_class_NXentry(self):
        expected_lines = '''
        **definition**: (optional) :ref:`NX_CHAR <NX_CHAR>`
        **DATA**: (optional) :ref:`NXdata`
        **notes**: (optional) :ref:`NXnote`
        **@default**: (optional) :ref:`NX_CHAR <NX_CHAR>`
        '''.strip().splitlines()
        
        self.apply_tests('base_classes', 'NXentry', expected_lines)
        
    def test_base_class_NXuser(self):
        expected_lines = '''
        **name**: (optional) :ref:`NX_CHAR <NX_CHAR>`
        '''.strip().splitlines()
        
        self.apply_tests('base_classes', 'NXuser', expected_lines)
        
    def test_application_definition_NXcanSAS(self):
        expected_lines = '''
        **definition**: (required) :ref:`NX_CHAR <NX_CHAR>`
        **title**: (required) :ref:`NX_CHAR <NX_CHAR>`
        **run**: (required) :ref:`NX_CHAR <NX_CHAR>`
        **I**: (required) :ref:`NX_NUMBER <NX_NUMBER>`
        **Q**: (required) :ref:`NX_NUMBER <NX_NUMBER>` {units=\ :ref:`NX_PER_LENGTH <NX_PER_LENGTH>`}
        **Idev**: (optional) :ref:`NX_NUMBER <NX_NUMBER>`
        **dQw**: (optional) :ref:`NX_NUMBER <NX_NUMBER>` {units=\ :ref:`NX_PER_LENGTH <NX_PER_LENGTH>`}
        **dQl**: (optional) :ref:`NX_NUMBER <NX_NUMBER>` {units=\ :ref:`NX_PER_LENGTH <NX_PER_LENGTH>`}
        **ENTRY**: (required) :ref:`NXentry`
        **DATA**: (required) :ref:`NXdata`
        **TRANSMISSION_SPECTRUM**: (optional) :ref:`NXdata`
        **SAMPLE**: (optional) :ref:`NXsample`
        **INSTRUMENT**: (optional) :ref:`NXinstrument`
        **NOTE**: (optional) :ref:`NXnote`
        **PROCESS**: (optional) :ref:`NXprocess`
        **SOURCE**: (optional) :ref:`NXsource`
        **@default**: (optional) :ref:`NX_CHAR <NX_CHAR>`
        **@timestamp**: (optional) :ref:`NX_DATE_TIME <NX_DATE_TIME>`
        **@canSAS_class**: (required) :ref:`NX_CHAR <NX_CHAR>`
        **@signal**: (required) :ref:`NX_CHAR <NX_CHAR>`
        **@I_axes**: (required) :ref:`NX_CHAR <NX_CHAR>`
        '''.strip().splitlines()
        
        self.apply_tests('applications', 'NXcanSAS', expected_lines)

    def apply_tests(self, category, class_name, expected_lines):
        nxdl_file = os.path.join(os.path.dirname(__file__),'..', category, class_name+'.nxdl.xml')
        self.assertTrue(os.path.exists(nxdl_file), nxdl_file)
        
        sys.argv.insert(0, 'python')
        with Capture_stdout() as printed_lines:
            nxdl2rst.print_rst_from_nxdl(nxdl_file)
        
        printed_lines = [_.strip() for _ in printed_lines]
        for line in expected_lines:
            expected = line.strip()
            self.assertTrue(expected in printed_lines, line.strip())


def suite(*args, **kw):
    '''gather all the tests together in a suite, called by run()'''
    test_suite = unittest.TestSuite()
    test_suite_list = [
        Issue_524_Clarify_Optional_or_Required,
    ]
    for item in test_suite_list:
        test_suite.addTests(unittest.makeSuite(item))
    return test_suite


def run():
    '''run all the unit tests'''
    runner=unittest.TextTestRunner(verbosity=2)
    runner.run(suite())


if __name__ == '__main__':
    run()
