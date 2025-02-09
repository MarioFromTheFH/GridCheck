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

from src.cmd_output import CMDOutput
from src.viergewinnt import check_for_win as CFW
from src.viergewinnt.metagame import Metagame

import unittest


class SimpleGridTest(unittest.TestCase):
    """
    Eine Testklasse für verschiedene Gitterkonfigurationen zur Überprüfung von
    Gewinnbedingungen

    """

    def setUp(self):
        """
        Initialisiert verschiedene Testgitter für diagonale, horizontale und vertikale Gewinnbedingungen.

        Die Gitter repräsentieren verschiedene Spielsituationen, die in den Testmethoden überprüft werden.
        """
        rows, cols = (6, 7)  # Definiert die Standardgröße des Spielfeldes (6 Reihen, 7 Spalten)

        # Erzeugt ein leeres Spielfeld, das mit `RESERVED` gefüllt ist
        self.emptygrid = [[Metagame.RESERVED for row in range(rows)] for col in range(cols)]

        # Testfälle für diagonale Gewinnmöglichkeiten mit drei gesetzten Steinen
        self.diagonal1_3 = [
            ["x", "0", "0", "0", "0", "0", "0"],
            ["0", "x", "0", "0", "0", "0", "0"],
            ["0", "0", "x", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0"]]

        self.diagonal2_3 = [
            ["0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "x", "0", "0", "0", "0"],
            ["0", "x", "0", "0", "0", "0", "0"],
            ["x", "0", "0", "0", "0", "0", "0"]]

        self.diagonal3_3 = [
            ["0", "0", "0", "0", "0", "0", "x"],
            ["0", "0", "0", "0", "0", "x", "0"],
            ["0", "0", "0", "0", "x", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0"]]

        self.diagonal4_3 = [
            ["0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "x", "0", "0", "0"],
            ["0", "0", "0", "0", "x", "0", "0"],
            ["0", "0", "0", "0", "0", "x", "0"]]

        # Testfälle für diagonale Gewinnmöglichkeiten mit vier gesetzten Steinen
        self.diagonal1 = [
            ["x", "0", "0", "0", "0", "0", "0"],
            ["0", "x", "0", "0", "0", "0", "0"],
            ["0", "0", "x", "0", "0", "0", "0"],
            ["0", "0", "0", "x", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0"]]

        self.diagonal2 = [
            ["0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "x", "0", "0", "0"],
            ["0", "0", "x", "0", "0", "0", "0"],
            ["0", "x", "0", "0", "0", "0", "0"],
            ["x", "0", "0", "0", "0", "0", "0"]]

        self.diagonal3 = [
            ["0", "0", "0", "0", "0", "0", "x"],
            ["0", "0", "0", "0", "0", "x", "0"],
            ["0", "0", "0", "0", "x", "0", "0"],
            ["0", "0", "0", "x", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0"]]

        self.diagonal4 = [
            ["0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "x", "0", "0", "0", "0"],
            ["0", "0", "0", "x", "0", "0", "0"],
            ["0", "0", "0", "0", "x", "0", "0"],
            ["0", "0", "0", "0", "0", "x", "0"]]

        # Testfälle für horizontale Gewinnmöglichkeiten
        self.horizontalnowin = [
            ["0", "0", "0", "0", "0", "x", "x"],
            ["x", "x", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0"]]

        self.horizontalwinx = [
            ["0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0"],
            ["x", "x", "x", "x", "0", "0", "0"]]

        self.horizontalwino = [
            ["0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0"],
            ["o", "o", "o", "o", "0", "0", "0"]]

        # Testfälle für vertikale Gewinnmöglichkeiten
        self.verticalwinx = [
            ["0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0"],
            ["x", "0", "0", "0", "0", "0", "0"],
            ["x", "0", "0", "0", "0", "0", "0"],
            ["x", "0", "0", "0", "0", "0", "0"],
            ["x", "0", "0", "0", "0", "0", "0"]]

        self.verticalwino = [
            ["0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0"],
            ["o", "0", "0", "0", "0", "0", "0"],
            ["o", "0", "0", "0", "0", "0", "0"],
            ["o", "0", "0", "0", "0", "0", "0"],
            ["o", "0", "0", "0", "0", "0", "0"]]

        self.verticalnowin = [
            ["0", "o", "0", "0", "0", "0", "0"],
            ["0", "o", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0"],
            ["o", "0", "0", "0", "0", "0", "0"],
            ["o", "0", "0", "0", "0", "0", "0"]]


    # ========================
    # Tests für diagonale Gewinne
    # ========================

    def test_diag1_only3(self):
        """ Testet, dass drei diagonale Steine keinen Gewinn auslösen. """
        cfw = CFW.CheckForWin()
        self.assertEqual(False, cfw.check_diagonally(self.diagonal1_3))

    def test_diag2_only3(self):
        """ Testet, dass drei diagonale Steine keinen Gewinn auslösen. """
        cfw = CFW.CheckForWin()
        self.assertEqual(False, cfw.check_diagonally(self.diagonal2_3))

    def test_diag3_only3(self):
        """ Testet, dass drei diagonale Steine keinen Gewinn auslösen. """
        cfw = CFW.CheckForWin()
        self.assertEqual(False, cfw.check_diagonally(self.diagonal3_3))

    def test_diag4_only3(self):
        """ Testet, dass drei diagonale Steine keinen Gewinn auslösen. """
        cfw = CFW.CheckForWin()
        self.assertEqual(False, cfw.check_diagonally(self.diagonal4_3))

    def test_diag1(self):
        """ Testet, dass vier diagonale 'x'-Steine einen Gewinn auslösen. """
        cfw = CFW.CheckForWin()
        self.assertEqual("x", cfw.check_diagonally(self.diagonal1))

    def test_diag2(self):
        """ Testet, dass vier diagonale 'x'-Steine einen Gewinn auslösen. """
        cfw = CFW.CheckForWin()
        self.assertEqual("x", cfw.check_diagonally(self.diagonal2))

    def test_diag3(self):
        """ Testet, dass vier diagonale 'x'-Steine einen Gewinn auslösen. """
        cfw = CFW.CheckForWin()
        self.assertEqual("x", cfw.check_diagonally(self.diagonal3))

    def test_diag4(self):
        """ Testet, dass vier diagonale 'x'-Steine einen Gewinn auslösen. """
        cfw = CFW.CheckForWin()
        self.assertEqual("x", cfw.check_diagonally(self.diagonal4))

    # ========================
    # Tests für vertikale Gewinne
    # ========================

    def test_CheckVerticalLeftWinX(self):
        """ Testet, dass vier vertikale 'x'-Steine einen Gewinn auslösen. """
        cfw = CFW.CheckForWin()
        self.assertEqual("x", cfw.check_vertically(self.verticalwinx))

    def test_CheckVerticalLeftWinO(self):
        """ Testet, dass vier vertikale 'o'-Steine einen Gewinn auslösen. """
        cfw = CFW.CheckForWin()
        self.assertEqual("o", cfw.check_vertically(self.verticalwino))

    def test_CheckVerticalDraw(self):
        """ Testet, dass ein leeres Spielfeld keinen vertikalen Gewinn auslöst. """
        cfw = CFW.CheckForWin()
        self.assertEqual(False, cfw.check_vertically(self.emptygrid))

    def test_CheckVerticalHorizontalWin(self):
        """ Testet, dass eine horizontale Gewinnreihe keinen vertikalen Gewinn auslöst. """
        cfw = CFW.CheckForWin()
        self.assertEqual(False, cfw.check_vertically(self.horizontalwinx))

    def test_CheckVerticalNoWin(self):
        """ Testet, dass ein unvollständiges vertikales Muster keinen Gewinn auslöst. """
        cfw = CFW.CheckForWin()
        self.assertEqual(False, cfw.check_vertically(self.verticalnowin))

    # ========================
    # Tests für horizontale Gewinne
    # ========================

    def test_CheckHorizontalNoWin(self):
        """ Testet, dass eine unvollständige horizontale Reihe keinen Gewinn auslöst. """
        cfw = CFW.CheckForWin()
        self.assertEqual(False, cfw.check_horizontally(self.horizontalnowin))

    def test_CheckHorizontalBottomWinX(self):
        """ Testet, dass eine vollständige horizontale 'x'-Reihe einen Gewinn auslöst. """
        cfw = CFW.CheckForWin()
        self.assertEqual("x", cfw.check_horizontally(self.horizontalwinx))

    def test_CheckHorizontalBottomWinO(self):
        """ Testet, dass eine vollständige horizontale 'o'-Reihe einen Gewinn auslöst. """
        cfw = CFW.CheckForWin()
        self.assertEqual("o", cfw.check_horizontally(self.horizontalwino))

    def test_CheckHorizontalBottomDraw(self):
        """ Testet, dass ein leeres Spielfeld keinen horizontalen Gewinn auslöst. """
        cfw = CFW.CheckForWin()
        self.assertEqual(False, cfw.check_horizontally(self.emptygrid))

    def test_CheckHorizontalBottomDrawVerticallyX(self):
        """ Testet, dass ein vertikaler Gewinn keinen horizontalen Gewinn auslöst. """
        cfw = CFW.CheckForWin()
        self.assertEqual(False, cfw.check_horizontally(self.verticalwinx))

    def test_CheckHorizontalBottomDrawVerticallyO(self):
        """ Testet, dass ein vertikaler Gewinn keinen horizontalen Gewinn auslöst. """
        cfw = CFW.CheckForWin()
        self.assertEqual(False, cfw.check_horizontally(self.verticalwino))


# ========================
# Zusätzliche Tests
# ========================

class WeirdGridTests(unittest.TestCase):
    """
    Testklasse für untypische oder unklare Spielsituationen.
    """

    def test_1(self):
        """ Dummy-Testfall zur Überprüfung der Testumgebung. """
        assert 1 == 1
