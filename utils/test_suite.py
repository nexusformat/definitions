#!/usr/bin/env python

"""
unit testing of the NeXus definitions
"""

import os
import unittest
import sys


def suite(*args, **kw):
    import test_nxdl
    import test_nxdl2rst

    test_suite = unittest.TestSuite()
    test_list = [
        test_nxdl,
        test_nxdl2rst,
    ]

    for test in test_list:
        test_suite.addTest(test.suite())
    return test_suite


if __name__ == "__main__":
    owd = os.getcwd()
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite())
    os.chdir(owd)
    sys.exit(len(result.errors))
