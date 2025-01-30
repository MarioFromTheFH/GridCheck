#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#############################################
# Author: Mario Schwaiger                   #
# Email: s54953@edu.campus02.at             #
# Created: 29.10.2024 17:44                 #
#############################################
__author__ = "Mario Schwaiger"
__credits__ = ["Mario Schwaiger","Andreas-Mihail Cojoc"]
__version__ = "0.1"
__maintainer__ = "Mario Schwaiger"
__email__ = "s54953@edu.campus02.at"
__status__ = "Development"

import logging
from test.cmd_output import CMDOutput as cmd

class CheckForWin():
    def __init__(self, wincnt=4, figset=["x","o"],reserved="0",drawretval=False):
        """Init Funktion 

        :param wincnt: Anzahl der benötigten Steine in einer Reihe zum Gewinnen
        :param figset: Array mit den existierenden, gültigen Steinen
        :param reserved: Zeichen für ein leeres Feld
        :param drawretval: Rückgabewert, falls (bisher) noch kein Spieler gewonnen hat
        :returns: 

        """
        #self.grid=grid
        self.wincnt=wincnt
        self.figset=figset
        self.reserved=reserved
        self.drawretval=drawretval

        logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.DEBUG, format='%(message)s')

    @property
    def figset(self):
        return self._figset

    @figset.setter
    def figset(self,figset):
        self._figset=figset

    
    def doCheck(self,grid):
        for method in (self.check_horizontally, self.check_vertically, self.check_diagonally):
            result = method(grid)
            if result is not False:  # Prüft, ob der Rückgabewert kein False ist
                return result
        return False  # Gibt None zurück, wenn alle Methoden False zurückgeben

    def isBoardFull(self,grid):
        ## If there are no empty spaces in the grid, return True
        for x in range(len(grid[0])):
            for y in range(len(grid)):  
                if grid[y][x] == self.reserved:
                    return False
        return True        

    def isValidMove(self, grid, column):
        ## Judge the validity of a piece's move
        if column < 0 or column >= (len(grid[0])) or grid[column][0] != self.reserved:
        ## If the column is less than 0 or greater than BOARDWIDTH, or there is no empty space in the column
            return False
            ## Then it is an invalid move, otherwise it is valid
        return True

    
    def check_diagonally(self,grid):
        """Überprüft das Feld, ob ein Sieger diagonal feststeht

        :returns: der Stein, der gewonnen hat, oder self.drawretval falls kein Sieger feststeht
        """

    def check_diagonal_winner(self, grid):
        dcount = [self.reserved, 0]  # Speichert das aktuelle Symbol und die Anzahl der aufeinanderfolgenden Vorkommen

        # Iteriert über alle Spalten (x-Koordinate)
        for x in range(len(grid[0])):
            # Iteriert über alle Zeilen (y-Koordinate)
            for y in range(len(grid)):
                dcount = [self.reserved, 0]  # Zurücksetzen des Zählers für jede neue Startposition

                # Prüft, ob das aktuelle Feld eine Spielfigur enthält
                if grid[y][x] in self.figset:
                    dcount = [grid[y][x], 1]  # Speichert das Symbol und setzt den Zähler auf 1

                    logging.debug(f"Found {grid[y][x]} at {x}|{y}")  # Debug-Log für die Position des Symbols

                    # Prüft die diagonale Gewinnbedingung in die positive Richtung (↘)
                    dres = self.check_diag_line_positiv(grid, x, y, dcount)
                    if dres != self.drawretval:  # Falls ein Gewinner gefunden wurde
                        return dres

                    dcount = [grid[y][x], 1]  # Zurücksetzen für die negative Diagonale

                    # Prüft die diagonale Gewinnbedingung in die negative Richtung (↙)
                    dres = self.check_diag_line_negativ(grid, x, y, dcount)
                    if dres != self.drawretval:  # Falls ein Gewinner gefunden wurde
                        return dres

        return self.drawretval  # Falls kein Gewinner gefunden wurde, Rückgabewert für Unentschieden oder Fortsetzung


def check_diag_line_negativ(self,grid,x,y,dcount):

        """Überprüft einen Stein darauf, ob in eine der Diagonalrichtungen ein Sieg feststeht. In Richtung der x-Achse wird hier nach oben gezählt, in Richtung der y-Achese wird heruntergezählt

        :param x: x-Koordinate des Steines der gefunden wurde
        :param y: y-Koordinate des Steines der gefunden wurde
        :param dcount: [Stein, Anzahl der gefundenen Steine --> Immer 1]
        :returns: der Stein der gewonnen hat, sonst self.drawretval

        """
#        Überprüfen auf OutOfBounds
        if x+(self.wincnt-1)>=len(grid[0]):
            return self.drawretval
        if y-(self.wincnt-1)<0:
            return self.drawretval    

        logging.debug(f"x:{x}\ny:{y}")
        logging.debug(cmd.doCMDOutput(grid))
        # import ipdb; ipdb.set_trace()
        for x_diag, y_diag in zip(range(x+1,x+self.wincnt),range(y-1,y-(self.wincnt),-1)):
            logging.debug(f"x_diag:{x_diag}\ny_diag:{y_diag}\ngrid[y][x]:{grid[y][x]}")

            if grid[y_diag][x_diag]==dcount[0]:
                dcount[1]+=1
                logging.debug(dcount[1])
                if dcount[1]>=self.wincnt:
                    return dcount[0]                    
            else:
                return self.drawretval  

    
    def check_diag_line_positiv(self,grid,x,y,dcount):
        """Überprüft einen Stein darauf, ob in eine der Diagonalrichtungen ein Sieg feststeht. Sowohl die x-Achse, als auch die y-Achse werden addiert. Dadurch werden Siege ermittelt die nach links oben oder rechts unten gefunden weren.

        :param x: x-Koordinate des Steines der gefunden wurde
        :param y: y-Koordinate des Steines der gefunden wurde
        :param dcount: [Stein, Anzahl der gefundenen Steine --> Immer 1]
        :returns: der Stein der gewonnen hat, sonst self.drawretval
        """

    def check_diagonal_winner(self, grid, x, y):
        # Überprüfen, ob die Diagonale über die Spielfeldgrenzen hinausgeht
        if x + self.wincnt - 1 >= len(grid[0]):  # Prüft, ob die x-Koordinate zu weit nach rechts geht
            return self.drawretval
        if y + self.wincnt - 1 >= len(grid):  # Prüft, ob die y-Koordinate zu weit nach unten geht
            return self.drawretval

        # Iteriere über die diagonalen Positionen nach rechts unten
        for x_diag, y_diag in zip(range(x + 1, x + self.wincnt), range(y + 1, y + self.wincnt)):
            # print(x_diag, y_diag, self.grid[x][y])  # Debugging-Zeile (auskommentiert)

            if grid[y_diag][x_diag] == dcount[0]:  # Falls das Symbol mit dem vorherigen übereinstimmt
                dcount[1] += 1  # Zähler erhöhen

                if dcount[1] >= self.wincnt:  # Falls die Gewinnanzahl erreicht wurde
                    return dcount[0]  # Gewinner zurückgeben

        return self.drawretval  # Falls kein Gewinner gefunden wurde, Rückgabewert für Unentschieden oder Fortsetzung


def check_vertically(self,grid):
        """Überprüft auf einen Sieg durch vertikal gelegte Steine

        :returns: der Stein der gewonnen hat, sonst self.drawretval
        """

    def check_vertical_winner(self, grid):
        vcount = [self.reserved, 0]  # Speichert das aktuelle Symbol und die Anzahl der aufeinanderfolgenden Vorkommen

        # Iteriere über die Spalten (y-Koordinate)
        for y in range(len(grid[0])):
            vcount = [self.reserved, 0]  # Zähler für jede neue Spalte zurücksetzen

            # Iteriere über die Zeilen (x-Koordinate)
            for x in range(len(grid)):
                if grid[x][y] == self.reserved:  # Falls die Zelle leer ist
                    vcount = [self.reserved, 1]  # Zähler zurücksetzen
                    continue  # Zum nächsten Element springen

                elif grid[x][y] in self.figset:  # Falls das Symbol eine gültige Spielfigur ist
                    if grid[x][y] == vcount[0]:  # Falls es mit dem vorherigen Symbol in der Spalte übereinstimmt
                        vcount[1] += 1  # Zähler erhöhen
                        if vcount[1] >= self.wincnt:  # Falls die Gewinnanzahl erreicht wurde
                            return grid[x][y]  # Gewinner zurückgeben
                    else:  # Falls das Symbol von der vorherigen Zelle abweicht
                        vcount[0] = grid[x][y]  # Neues Symbol speichern
                        vcount[1] = 1  # Zähler zurücksetzen

        return self.drawretval  # Falls kein Gewinner gefunden wurde, Rückgabewert für Unentschieden oder Fortsetzung

    def check_horizontally(self,grid):
        """Überprüft auf einen Sieg durch horizontal gelegt Steine

        :returns: der Stein der gewonnen hat, sonst self.drawretval
        """

    def check_winner(self, grid):
        for row in grid:  # Durchläuft jede Zeile im Spielfeld
            hcount = [self.reserved,
                      0]  # Speichert das aktuelle Symbol und die Anzahl der aufeinanderfolgenden Vorkommen
            for coin in row:  # Durchläuft jede Spalte der aktuellen Zeile
                if coin == self.reserved:  # Falls die Zelle leer ist
                    hcount = [self.reserved, 1]  # Zähler zurücksetzen
                elif coin in self.figset:  # Falls das Symbol eine gültige Spielfigur ist
                    if coin == hcount[0]:  # Falls es mit dem vorherigen Symbol übereinstimmt
                        hcount[1] += 1  # Zähler erhöhen
                        if hcount[1] >= self.wincnt:  # Falls die Gewinnanzahl erreicht wurde
                            return coin  # Gewinner zurückgeben
                    else:  # Falls das Symbol von der vorherigen Zelle abweicht
                        hcount[0] = coin  # Neues Symbol speichern
                        hcount[1] = 1  # Zähler zurücksetzen
        return self.drawretval  # Falls kein Gewinner gefunden wurde, Rückgabewert für Unentschieden oder Fortsetzung


