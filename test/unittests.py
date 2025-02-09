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

import unittest
import sys
import test_grids  # Importiert das Testmodul, das die Testfälle enthält

if __name__ == '__main__':
    """
    Führt eine Test-Suite mit Unittest aus, lädt Tests aus dem Modul `test_grids` 
    und gibt detaillierte Testergebnisse aus.

    Das Skript lädt die Testfälle, führt sie aus und gibt Fehler, Fehlschläge und 
    übersprungene Tests aus. Am Ende wird das Skript mit einer Fehleranzahl als 
    Exit-Code beendet.
    """

    # Erstellt eine Test-Suite
    suite = unittest.TestSuite()

    # Erstellt einen TestLoader zum Laden der Testfälle aus `test_grids`
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromModule(test_grids))

    # Erstellt einen TestRunner zur Ausführung der Tests mit detaillierter Ausgabe
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Detaillierte Fehlerausgabe
    if result.errors:
        print("\n======== Errors ==========")
        for test, err in result.errors:
            print(f"In {test}:\n{err}")

    # Detaillierte Ausgabe von fehlgeschlagenen Tests
    if result.failures:
        print("\n=========== Failures ============")
        for test, err in result.failures:
            print(f"In {test}:\n{err}")

    # Ausgabe übersprungener Tests
    if result.skipped:
        print("\n=========== Skipped ============")
        for test, reason in result.skipped:
            print(f"In {test}:\n{reason}")

    # Beenden des Skripts mit der Anzahl der Fehler und Fehlschläge als Exit-Code
    sys.exit(len(result.errors) + len(result.failures))

