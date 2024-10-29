#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#############################################
# Author: Mario Schwaiger                   #
# Email: s54953@edu.campus02.at             #
# Created: 29.10.2024 17:44                 #
#############################################
__author__ = "Mario Schwaiger"
__credits__ = ["Mario Schwaiger"]
__version__ = "0.1"
__maintainer__ = "Mario Schwaiger"
__email__ = "s54953@edu.campus02.at"
__status__ = "Development"
    

class CheckForWin():
    def __init__(self, grid, wincnt=4, figset=["x","o"],reserved="0",drawretval=False):
        self.grid=grid
        self.wincnt=wincnt
        self.figset=figset
        self.reserved=reserved
        self.drawretval=drawretval

    def checkDiagonally(self):
        dcount=[self.reserved,0]
        for x in range(len(self.grid)):
            for y in range(len(self.grid[0])):
                dcount=[self.reserved,0]
                #Geht durch, bis er ein Element findet
                if self.grid[x][y] in self.figset:
                    dcount=[self.grid[x][y],1]
                                      
                    print(f"Found {self.grid[x][y]} at {x}|{y}")
                    dres=self.checkDiagLinePositiv(x,y,dcount)
                    if dres != self.drawretval:
                        return dres
                                
        return self.drawretval                

    def checkDiagLinePositiv(self,x,y,dcount):

        #Überprüfen auf OutOfBounds
        if x+self.wincnt>len(self.grid):
            return self.drawretval
        if y+self.wincnt>len(self.grid[0]):
            return self.drawretval
        
        for x_diag, y_diag in zip(range(x+1,x+self.wincnt),range(y+1,y+self.wincnt)):
            print(x_diag,y_diag,self.grid[x][y])
            if self.grid[x_diag][y_diag]==dcount[0]:
                dcount[1]+=1
                if dcount[1]>=self.wincnt:
                    return dcount[0]
                    
        return self.drawretval  
    

                    
                
            

    def checkVertically(self):
        vcount=[self.reserved,0]
        for y in range(len(self.grid[0])):
            vcount=[self.reserved,0]
            for x in range(len(self.grid)):
                if self.grid[x][y] == self.reserved:
                    vcount=[self.reserved,1]
                    continue
                elif self.grid[x][y] in self.figset:
                    if self.grid[x][y] == vcount[0]:
                        vcount[1]+=1
                        if vcount[1]>=self.wincnt:
                            return self.grid[x][y]
                    else:
                        vcount[0]=self.grid[x][y]
                        vcount[1]=1
        return self.drawretval
            
            
    def checkHorizontally(self):
        hcount=[self.reserved,0]
        for row in self.grid:
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

