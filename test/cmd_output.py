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


class CMDOutput():
    # Statische Methode, um eine formatierte String-Darstellung des Grids zu erzeugen
    @staticmethod
    def doCMDOutput(grid):
        outputstring = ""  # Initialisiere einen leeren String, der die formatierte Ausgabe speichern wird

        # Schleife über die Reihen im Grid in umgekehrter Reihenfolge (beginnt mit der letzten Reihe)
        for row in reversed(grid):
            outputstring += "|"  # Füge ein senkrechtes Strichzeichen vor jeder Reihe hinzu, um die Spaltenränder darzustellen

            # Schleife über jedes Coin (oder Element) in der Reihe
            for coin in row:
                outputstring += coin  # Füge den Wert des Coins zum Ausgabe-String hinzu (z.B. "x", "o" oder "0")
                outputstring += "|"  # Füge nach jedem Coin ein senkrechtes Strichzeichen hinzu, um die Spaltenränder darzustellen

            outputstring += "\n"  # Nachdem jede Reihe verarbeitet wurde, füge einen Zeilenumbruch hinzu, um zur nächsten Reihe zu wechseln

        return outputstring  # Gib den formatierten String zurück, der das Grid darstellt
