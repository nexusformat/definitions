# advice: http://stackoverflow.com/questions/191673/preferred-python-unit-testing-framework?rq=1
# advice: http://stackoverflow.com/questions/17001010/how-to-run-unittest-discover-from-python-setup-py-test#21726329
# advice: http://stackoverflow.com/questions/6164004/python-package-structure-setup-py-for-running-unit-tests?noredirect=1&lq=1


import os
import unittest
import sys

# _path = os.path.join(os.path.dirname(__file__), '..',)
# if _path not in sys.path:
#     sys.path.insert(0, _path)
# from tests import common


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


if __name__ == '__main__':
    runner=unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
