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


class CMDOutput:
    """
    Eine Klasse zur Darstellung eines Gitters als Zeichenkettenausgabe für die Konsole.
    """

    @staticmethod
    def doCMDOutput(grid):
        """
        Erstellt eine textbasierte Darstellung des Gitters.

        Diese Methode nimmt ein zweidimensionales Array `grid` entgegen und formatiert es
        als Zeichenkette mit Spaltentrennzeichen (`|`), wobei die Reihen von unten nach oben
        dargestellt werden.

        Parameters
        ----------
        grid : list of list of str
            Eine 2D-Liste, die das Raster repräsentiert. Jedes Element ist ein Zeichen,
            das z. B. eine Spielfigur oder ein leeres Feld darstellen kann.

        Returns
        -------
        str
            Die formatierte Zeichenkettenrepräsentation des Gitters, bereit für die
            Konsolenausgabe.
        """
        outputstring = ""  # Initialisierung der Ausgabekette

        # Iteration durch das Gitter von unten nach oben
        for row in reversed(grid):
            outputstring += "|"  # Beginn der Zeile mit einem Spaltentrennzeichen

            # Iteration durch die Elemente der aktuellen Zeile
            for coin in row:
                outputstring += coin  # Hinzufügen des Symbols zur Zeichenkette
                outputstring += "|"  # Spaltentrenner nach jedem Symbol

            outputstring += "\n"  # Zeilenumbruch nach jeder Reihe

        return outputstring  # Rückgabe der formatierten Zeichenkette

