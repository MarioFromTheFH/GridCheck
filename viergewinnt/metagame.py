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

from test.cmd_output import CMDOutput as cmdo

class Metagame():

    COIN_PLAYER_1='x'
    COIN_PLAYER_2='o'
    FIGSET=[COIN_PLAYER_1,COIN_PLAYER_2]
    
    RESERVED="0"
    
    def create_board(self, cols,rows):
        return [[self.RESERVED for col in range(cols)] for row in range(rows)]

    def is_valid_location(self, grid, col, row_count):
        return grid[row_count-1][col] == self.RESERVED

    def isValidMove(self, grid, column):
        ## Judge the validity of a piece's move

        if column>=len(grid):
            return False
        
        if column < 0:
        ## If the column is less than 0 or greater than BOARDWIDTH, or there is no empty space in the column
            return False

        if grid[len(grid)-1][column]!=self.RESERVED:
            return False

        return True    

    
    def get_next_open_row(self,board, col, row_count):
        cmdo.doCMDOutput(board)
        print("Row Count:"+str(row_count))
        for r in range(row_count):
            if board[r][col] == self.RESERVED:
                return r

        print("Return -1")
        return -1
            
    def drop_piece(self, row, col, piece):
        self.board[row][col] = piece    

    
    def makeMove(self,board, player, column):
        lowest = self.get_next_open_row(board, column, len(board[0]))
        if lowest != -1:
            print("col: "+str(column))
            print("row: "+str(lowest))
            board[column][lowest] = player
