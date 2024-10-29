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

        self.horizontalnowin=[
            ["0","0","0","0","0","x","x"],
            ["x","x","0","0","0","0","0"],
            ["0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0"]]
        
        self.horizontalwinx=[
            ["0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0"],
            ["x","x","x","x","0","0","0"]]
        self.horizontalwino=[
            ["0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0"],
            ["o","o","o","o","0","0","0"]]
        self.verticalwinx=[
            ["0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0"],
            ["x","0","0","0","0","0","0"],
            ["x","0","0","0","0","0","0"],
            ["x","0","0","0","0","0","0"],
            ["x","0","0","0","0","0","0"]]
        self.verticalwino=[
            ["0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0"],
            ["o","0","0","0","0","0","0"],
            ["o","0","0","0","0","0","0"],
            ["o","0","0","0","0","0","0"],
            ["o","0","0","0","0","0","0"]]        

    def test_CheckVerticalLeftWinX(self):
        cfw=CFW.CheckForWin(self.verticalwinx)
        self.assertEqual("x",cfw.checkVertically())

    def test_CheckVerticalLeftWinO(self):
        cfw=CFW.CheckForWin(self.verticalwino)
        self.assertEqual("o",cfw.checkVertically())        

    def test_CheckVerticalDraw(self):
        cfw=CFW.CheckForWin(self.emptygrid)
        self.assertEqual(False,cfw.checkVertically())

    def test_CheckVerticalHorizontalWin(self):
        cfw=CFW.CheckForWin(self.horizontalwinx)
        self.assertEqual(False,cfw.checkVertically())          

# Horizontale Testcases
    def test_CheckHorizontalNoWin(self):
        cfw=CFW.CheckForWin(self.horizontalnowin)
        self.assertEqual(False,cfw.checkHorizontally())
        
    def test_CheckHorizontalBottomWinX(self):
        cfw=CFW.CheckForWin(self.horizontalwinx)
        self.assertEqual("x",cfw.checkHorizontally())

    def test_CheckHorizontalBottomWinO(self):
        cfw=CFW.CheckForWin(self.horizontalwino)
        self.assertEqual("o",cfw.checkHorizontally())        

    def test_CheckHorizontalBottomDraw(self):
        cfw=CFW.CheckForWin(self.emptygrid)
        self.assertEqual(False,cfw.checkHorizontally())

    def test_CheckHorizontalBottomDrawVerticallyX(self):
        cfw=CFW.CheckForWin(self.verticalwinx)
        self.assertEqual(False,cfw.checkHorizontally())
        
    def test_CheckHorizontalBottomDrawVerticallyO(self):
        cfw=CFW.CheckForWin(self.verticalwino)
        self.assertEqual(False,cfw.checkHorizontally())           


    def no_test_cmd_output(self):
        CMDOutput.doCMDOutput(self.grid)

class WeirdGridTests(unittest.TestCase):
    def test_1(self):
        assert 1==1

