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

from Tests import GridTests# import SimpleGridTest, WeirdGridTests
#import EnhancedTestDeco as etd
#from ETDConstants import TESTINGCOLORSCOLORS
#import ETDConstants as ehconst

import unittest
import os.path
from os import path
import os
import sys

suite = unittest.TestSuite()
loader = unittest.TestLoader()


suite.addTests(loader.loadTestsFromModule(GridTests))
#suite.addTests(loader.loadTestsFromModule(WeirdGridTests))

if __name__ == '__main__':

    # etd.TESTINGCOLORS = {
    #     'ExampleTest': TESTINGCOLORSCOLORS['Red'],
    #     'Tests.MoreTests' : TESTINGCOLORSCOLORS['Green'],
    # }

    # dc = etd.DecoWrapper([ExampleTest,
    #     MoreTests],
    #     "test")

    file_and_path = os.path.join(os.getcwd(), "report.txt")
    f = open(file_and_path, "w+")
    f.write(str(0))
    f.close()
    runner = unittest.TextTestRunner(resultclass=unittest.TestResult)
    res = runner.run(suite)
    os.remove(file_and_path)

    nr_errors = len(res.errors)
    nr_failures = len(res.failures)

    if nr_errors > 0:
        print("======== Errors ==========")
        for err, msg in res.errors:
            print("In ", err, ":\n\n", msg)
    if nr_failures > 0:
        print("=========== Failures ============== ")
        for err, msg in res.failures:
            print("In ", err, ":\n\n", msg)
    if len(res.skipped) > 0:
        print("=========== Skipped ============== ")
        for err, msg in res.skipped:
            print("In ", err, ":\n\n", msg)

    # Print summary
    if nr_errors > 0:
        print('\n\n')
        print("Errors in:\n\n")
        for err, msg in res.errors:
            print(err, '\n')

    print()
    if nr_failures > 0:
        print('\n\n')
        print("Failures in\n\n")
        for err, msg in res.failures:
            print(err, '\n')
    print()

    sys.exit(nr_errors + nr_failures)
