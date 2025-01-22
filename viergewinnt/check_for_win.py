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
        logging.basicConfig(level=logging.WARNING, format='%(message)s')

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
    
    def check_diagonally(self,grid):
        """Überprüft das Feld, ob ein Sieger diagonal feststeht

        :returns: der Stein, der gewonnen hat, oder self.drawretval falls kein Sieger feststeht
        """
        
        dcount=[self.reserved,0]
        for x in range(len(grid[0])):
            for y in range(len(grid)):            
                dcount=[self.reserved,0]
                #Geht durch, bis er ein Element findet
                if grid[y][x] in self.figset:
                    dcount=[grid[y][x],1]
                                      
                    logging.debug(f"Found {grid[y][x]} at {x}|{y}")
                    dres=self.check_diag_line_positiv(grid,x,y,dcount)
                    if dres != self.drawretval:
                        return dres

                    dcount=[grid[y][x],1]
                    dres=self.check_diag_line_negativ(grid,x,y,dcount)
                    if dres != self.drawretval:
                        return dres
                    
        return self.drawretval                


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
        
        #Überprüfen auf OutOfBounds
        if x+self.wincnt-1>=len(grid[0]):
            return self.drawretval
        if y+self.wincnt-1>=len(grid):
            return self.drawretval
        
        for x_diag, y_diag in zip(range(x+1,x+self.wincnt),range(y+1,y+self.wincnt)):
#            print(x_diag,y_diag,self.grid[x][y])
            if grid[y_diag][x_diag]==dcount[0]:
                dcount[1]+=1
                if dcount[1]>=self.wincnt:
                    return dcount[0]
                    
        return self.drawretval  
    

    def check_vertically(self,grid):
        """Überprüft auf einen Sieg durch vertikal gelegte Steine

        :returns: der Stein der gewonnen hat, sonst self.drawretval
        """
        
        vcount=[self.reserved,0]
        for y in range(len(grid[0])):
            vcount=[self.reserved,0]
            for x in range(len(grid)):
                if grid[x][y] == self.reserved:
                    vcount=[self.reserved,1]
                    continue
                elif grid[x][y] in self.figset:
                    if grid[x][y] == vcount[0]:
                        vcount[1]+=1
                        if vcount[1]>=self.wincnt:
                            return grid[x][y]
                    else:
                        vcount[0]=grid[x][y]
                        vcount[1]=1
        return self.drawretval
            
            
    def check_horizontally(self,grid):
        """Überprüft auf einen Sieg durch horizontal gelegt Steine

        :returns: der Stein der gewonnen hat, sonst self.drawretval
        """
        
        hcount=[self.reserved,0]
        for row in grid:
            #Leeren, wenn neue Reihe beginnt
            hcount=[self.reserved,0] 
            for col in row:
                for coin in col:
                    #Zelle ist leer
                    if coin == self.reserved: 
                        hcount=[self.reserved,1]
                        continue
                    #Zelle ist dasselbe wie in voriger Zelle
                    elif coin in self.figset:   
                        if coin == hcount[0]:
                            hcount[1]+=1
                            if hcount[1]>=self.wincnt:
                                return coin
                        #Zelle hat etwas Anderes   
                        else:             
                            hcount[0]=coin
                            hcount[1]=1
        return self.drawretval

