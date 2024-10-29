#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#############################################
# Author: Mario Schwaiger                   #
# Email: s54953@edu.campus02.at             #
# Created: 29.10.2024 17:50                 #
#############################################
__author__ = "Mario Schwaiger"
__credits__ = ["Mario Schwaiger"]
__version__ = "0.1"
__maintainer__ = "Mario Schwaiger"
__email__ = "s54953@edu.campus02.at"
__status__ = "Development"

import unittest
from .CMDOutput import CMDOutput
import CheckForWin as CFW

class SimpleGridTest(unittest.TestCase):

    def setUp(self):
        rows, cols = (6, 7)
        self.emptygrid = [["0"]*cols]*rows
        self.horizontalwin=[["0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0"],
            ["x","x","x","x","0","0","0"]]
        self.verticalwin=[["0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0"],
            ["x","0","0","0","0","0","0"],
            ["x","0","0","0","0","0","0"],
            ["x","0","0","0","0","0","0"],
            ["x","0","0","0","0","0","0"]]
    
    def test_CheckHorizontalBottomWin(self):
        cfw=CFW.CheckForWin(self.horizontalwin)
        self.assertEqual("x",cfw.checkHorizontally())

    def test_CheckHorizontalBottomDraw(self):
        cfw=CFW.CheckForWin(self.emptygrid)
        self.assertEqual(False,cfw.checkHorizontally())

    def test_CheckHorizontalBottomDrawVertically(self):
        cfw=CFW.CheckForWin(self.verticalwin)
        self.assertEqual(False,cfw.checkHorizontally())        
        

    def test_assertFalse(self):
        self.assertFalse(False)

    def no_test_cmd_output(self):
        CMDOutput.doCMDOutput(self.grid)

class WeirdGridTests(unittest.TestCase):
    def test_1(self):
        assert 1==1

