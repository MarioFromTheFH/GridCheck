#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#############################################
# Author: Mario Schwaiger                   #
# Email: s54953@edu.campus02.at             #
# Created: 29.10.2024 18:50                 #
#############################################
__author__ = "Mario Schwaiger"
__credits__ = ["Mario Schwaiger"]
__version__ = "0.1"
__maintainer__ = "Mario Schwaiger"
__email__ = "s54953@edu.campus02.at"
__status__ = "Development"

from test import test_grids
#import EnhancedTestDeco as etd
#from ETDConstants import TESTINGCOLORSCOLORS
#import ETDConstants as ehconst

import unittest
import os.path
from os import path
import os
import sys


#suite.addTests(loader.loadTestsFromModule(WeirdGridTests))

if __name__ == '__main__':
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromModule(test_grids))

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Handle and print detailed results
    if result.errors:
        print("\n======== Errors ==========")
        for test, err in result.errors:
            print(f"In {test}:\n{err}")

    if result.failures:
        print("\n=========== Failures ============")
        for test, err in result.failures:
            print(f"In {test}:\n{err}")

    if result.skipped:
        print("\n=========== Skipped ============")
        for test, reason in result.skipped:
            print(f"In {test}:\n{reason}")

    # Exit with error count
    sys.exit(len(result.errors) + len(result.failures))
