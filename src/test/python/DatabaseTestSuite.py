'''
File: DatabaseTestSuite.py
Project: DevOps
Author: Dylan Greene
Created: 04/11/2026
Copyright (c) 2026 Dylan Greene
'''

# AI used to generate code for this test suite
import unittest

from src.test.python.EditInDatabaseTest import TestCreateShow
from src.test.python.GetFromDatabaseTest import TestGetUserId


def suite():
    test_suite = unittest.TestSuite()

    test_suite.addTests(
        unittest.defaultTestLoader.loadTestsFromTestCase(TestCreateShow)
    )

    test_suite.addTests(
        unittest.defaultTestLoader.loadTestsFromTestCase(TestGetUserId)
    )

    return test_suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())