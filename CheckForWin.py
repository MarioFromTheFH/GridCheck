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
    def __init__(self, grid, wincnt=4, figset=["x","o"],reserved="0"):
        self.grid=grid
        self.wincnt=wincnt
        self.figset=figset
        self.reserved=reserved

    def checkHorizontally(self,drawretval=False):
        hcount=[self.reserved,0]
        val=0
        for row in self.grid:
            for col in row:
                for coin in col:
                    if coin == self.reserved: #Zelle ist leer
                        hcount=[self.reserved,1]
                        continue
                    if coin in self.figset:   #Zelle ist dasselbe wie in voriger Zelle
                        if coin == hcount[0]:
                            hcount[1]+=1
                            if hcount[1]>=self.wincnt:
                                return coin
                        else:             #Zelle hat etwas Anderes
                            hcount[0]=coin
                            hcount[1]=1
        return drawretval

