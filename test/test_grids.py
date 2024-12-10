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
from .cmd_output import CMDOutput
import viergewinnt.check_for_win as CFW

class SimpleGridTest(unittest.TestCase):

    def setUp(self):
        rows, cols = (6, 7)
        self.emptygrid = [["0"]*cols]*rows

        self.diagonal1_3=[
            ["x","0","0","0","0","0","0"],
            ["0","x","0","0","0","0","0"],
            ["0","0","x","0","0","0","0"],
            ["0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0"]]
        self.diagonal2_3=[
            ["0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0"],
            ["0","0","x","0","0","0","0"],
            ["0","x","0","0","0","0","0"],
            ["x","0","0","0","0","0","0"]]
        self.diagonal3_3=[
            ["0","0","0","0","0","0","x"],
            ["0","0","0","0","0","x","0"],
            ["0","0","0","0","x","0","0"],
            ["0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0"]]
        self.diagonal4_3=[
            ["0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0"],
            ["0","0","0","x","0","0","0"],
            ["0","0","0","0","x","0","0"],
            ["0","0","0","0","0","x","0"]] 
        self.diagonal1=[
            ["x","0","0","0","0","0","0"],
            ["0","x","0","0","0","0","0"],
            ["0","0","x","0","0","0","0"],
            ["0","0","0","x","0","0","0"],
            ["0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0"]]
        self.diagonal2=[
            ["0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0"],
            ["0","0","0","x","0","0","0"],
            ["0","0","x","0","0","0","0"],
            ["0","x","0","0","0","0","0"],
            ["x","0","0","0","0","0","0"]]
        self.diagonal3=[
            ["0","0","0","0","0","0","x"],
            ["0","0","0","0","0","x","0"],
            ["0","0","0","0","x","0","0"],
            ["0","0","0","x","0","0","0"],
            ["0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0"]]
        self.diagonal4=[
            ["0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0"],
            ["0","0","x","0","0","0","0"],
            ["0","0","0","x","0","0","0"],
            ["0","0","0","0","x","0","0"],
            ["0","0","0","0","0","x","0"]]        
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
        self.verticalnowin=[
            ["0","o","0","0","0","0","0"],
            ["0","o","0","0","0","0","0"],
            ["0","0","0","0","0","0","0"],
            ["0","0","0","0","0","0","0"],
            ["o","0","0","0","0","0","0"],
            ["o","0","0","0","0","0","0"]]


    def test_diag1_only3(self):
        cfw=CFW.CheckForWin(self.diagonal1_3)
        self.assertEqual(False,cfw.checkDiagonally())

    def test_diag2_only3(self):
        cfw=CFW.CheckForWin(self.diagonal2_3)
        self.assertEqual(False,cfw.checkDiagonally())

    def test_diag3_only3(self):
        cfw=CFW.CheckForWin(self.diagonal3_3)
        self.assertEqual(False,cfw.checkDiagonally())

    def test_diag4_only3(self):
        cfw=CFW.CheckForWin(self.diagonal4_3)
        self.assertEqual(False,cfw.checkDiagonally())
        
    def test_diag1(self):
        cfw=CFW.CheckForWin(self.diagonal1)
        self.assertEqual("x",cfw.checkDiagonally())

    def test_diag2(self):
        cfw=CFW.CheckForWin(self.diagonal2)
        self.assertEqual("x",cfw.checkDiagonally())

    def test_diag3(self):
        cfw=CFW.CheckForWin(self.diagonal3)
        self.assertEqual("x",cfw.checkDiagonally())

    def test_diag4(self):
        cfw=CFW.CheckForWin(self.diagonal4)
        self.assertEqual("x",cfw.checkDiagonally())

# Vertikale Tests        

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

    def test_CheckVerticalNoWin(self):
        cfw=CFW.CheckForWin(self.verticalnowin)
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

