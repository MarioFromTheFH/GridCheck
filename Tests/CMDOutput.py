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
    @staticmethod
    def doCMDOutput(grid):
        outputstring=""
        for row in grid:
            outputstring+="|"
            for coin in row:
                outputstring+=coin
                outputstring+="|"
                
            outputstring+="\n"

        print(outputstring)
