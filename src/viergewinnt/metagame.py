#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#############################################
# Author: Mario Schwaiger                   #
# Email: s54953@edu.campus02.at             #
# Created: 21.01.2025 17:44                 #
#############################################
__author__ = "Mario Schwaiger"
__credits__ = ["Mario Schwaiger","Andreas-Mihail Cojoc"]
__version__ = "0.1"
__maintainer__ = "Mario Schwaiger"
__email__ = "s54953@edu.campus02.at"
__status__ = "Development"

from cmd_output import CMDOutput as cmdo


class Metagame():
    """
    Eine Klasse zur Verwaltung eines 2D-Grid-basierten Spiels.
    """

    COIN_PLAYER_1 = 'x'  # Symbol für Spieler 1
    COIN_PLAYER_2 = 'o'  # Symbol für Spieler 2
    FIGSET = [COIN_PLAYER_1, COIN_PLAYER_2]  # Mögliche Spielfiguren

    RESERVED = "0"  # Zeichen für freie Spielfelder

    def create_board(self, cols, rows):
        """
        Erstellt ein Spielfeld mit den angegebenen Spalten und Zeilen.

        Parameters
        ----------
        cols : int
            Anzahl der Spalten im Spielfeld.
        rows : int
            Anzahl der Reihen im Spielfeld.

        Returns
        -------
        list
            Ein 2D-Array, das das Spielfeld darstellt.
        """
        return [[self.RESERVED for col in range(cols)] for row in range(rows)]

    def is_valid_location(self, grid, col, row_count):
        """
        Überprüft, ob eine Spalte noch Platz für einen Spielstein hat.

        Parameters
        ----------
        grid : list
            Das aktuelle Spielfeld als 2D-Array.
        col : int
            Die Spalte, die überprüft wird.
        row_count : int
            Die Anzahl der Reihen im Spielfeld.

        Returns
        -------
        bool
            True, wenn ein Stein in dieser Spalte platziert werden kann, sonst False.
        """
        return grid[row_count - 1][col] == self.RESERVED

    def isValidMove(self, grid, column):
        """
        Prüft, ob ein Zug gültig ist.

        Ein Zug ist ungültig, wenn:
        - Die Spalte außerhalb des gültigen Bereichs liegt.
        - Die Spalte bereits voll ist.

        Parameters
        ----------
        grid : list
            Das Spielfeld als 2D-Array.
        column : int
            Die Spalte, in die der Stein gesetzt werden soll.

        Returns
        -------
        bool
            True, wenn der Zug gültig ist, sonst False.
        """
        if column >= len(grid):  # Spalte ist größer als die Breite des Spielfelds
            return False

        if column < 0:  # Spalte ist kleiner als 0
            return False

        if grid[len(grid) - 1][column] != self.RESERVED:  # Spalte ist bereits voll
            return False

        return True

    def get_next_open_row(self, board, col, row_count):
        """
        Findet die erste verfügbare Reihe in einer bestimmten Spalte.

        Parameters
        ----------
        board : list
            Das Spielfeld als 2D-Array.
        col : int
            Die Spalte, in der nach einer freien Reihe gesucht wird.
        row_count : int
            Die Anzahl der Reihen im Spielfeld.

        Returns
        -------
        int
            Die erste verfügbare Reihe (Index) oder -1, wenn die Spalte voll ist.
        """
        cmdo.doCMDOutput(board)  # Externer Funktionsaufruf (nicht definiert im Code)
        print("Row Count:" + str(row_count))
        for r in range(row_count):
            if board[r][col] == self.RESERVED:
                return r

        print("Return -1")
        return -1  # Keine freien Felder in dieser Spalte

    def drop_piece(self, row, col, piece):
        """
        Platziert einen Spielstein auf dem Spielfeld.

        Parameters
        ----------
        row : int
            Die Zeile, in die der Spielstein gesetzt wird.
        col : int
            Die Spalte, in die der Spielstein gesetzt wird.
        piece : str
            Der Spielstein ('x' oder 'o').

        Returns
        -------
        None
        """
        self.board[row][col] = piece

    def makeMove(self, board, player, column):
        """
        Führt einen Spielzug aus, indem ein Spielstein in eine Spalte gesetzt wird.

        Parameters
        ----------
        board : list
            Das aktuelle Spielfeld als 2D-Array.
        player : str
            Der Spielstein ('x' oder 'o').
        column : int
            Die Spalte, in die der Spielstein gesetzt wird.

        Returns
        -------
        None
        """
        lowest = self.get_next_open_row(board, column, len(board[0]))
        if lowest != -1:
            print("col: " + str(column))
            print("row: " + str(lowest))
            board[column][lowest] = player  # Setzt den Spielstein in die Spalte
