#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#############################################
# Author: Mario Schwaiger                   #
# Email: s54953@edu.campus02.at             #
# Created: 21.01.2025 17:28                 #
#############################################
__author__ = "Mario Schwaiger"
__credits__ = ["Mario Schwaiger","Andreas-Mihail Cojoc"]
__version__ = "0.1"
__maintainer__ = "Mario Schwaiger"
__email__ = "s54953@edu.campus02.at"
__status__ = "Development"

from viergewinnt.metagame import Metagame
import copy
import random

class AIMoves(Metagame):

    def __init__(self,cfw,difficulty=4):
        self.cfw=cfw
        self.difficulty=difficulty


    #Stolen from:https://towardsdatascience.com/beating-connect-four-with-ai-b88b220ff0f0
    def get_best_move(self, board , num_sims: int):

        # Get a list of all viable moves
        print("Len Board: "+str(len(board)))
        win_counts = {column: 0 for column in range(len(board[0])) if self.isValidMove(board,column)}
        total_counts = {column: 0 for column in range(len(board[0])) if self.isValidMove(board,column)}

        valid_moves = list(win_counts.keys())
        print("Valid Moves: "+str(valid_moves))
        for _ in range(num_sims):
            column = random.choice(valid_moves) # Pick a move a random
            dupeBoard = copy.deepcopy(board)
            print("Column: "+str(column))
            self.makeMove(dupeBoard, self.cfw.figset[1], column)
            result = self.cfw.doCheck(dupeBoard) # Simulate the game after making the random move
            total_counts[column] += 1
            if result == self.cfw.figset[1]: # Check whether the AI player won
                win_counts[column] += 1

        win_rates = {column: win_counts[column] / total_counts[column] if total_counts[column] > 0 else 0 for column in valid_moves}
        best_move = max(win_rates, key=win_rates.get) # Find the move with the best win rate
        print("Best Move: "+str(best_move))
        return best_move        
        

    #Stolen from https://labex.io/tutorials/python-connect-four-game-human-vs-ai-298858
    def getPotentialMoves(self,board, tile, lookAhead):
        if lookAhead == 0 or self.cfw.isBoardFull(board):
            '''
            If the difficulty coefficient is 0 or the board is full,
            return a list with all values set to 0. This means that
            the fitness value is equal to the potential moves for each column.
            In this case, AI will drop the piece randomly and lose its intelligence.
            '''
            return [0] * len(board[0])

        ## Determine the color of the opponent's piece
        if tile == self.cfw.figset[0]:
            enemyTile = self.cfw.figset[1]
        else:
            enemyTile = self.cfw.figset[0]
        potentialMoves = [0] * len(board[0])
        ## Initialize a list of potential moves, with all values set to 0
        for firstMove in range(len(board[0])):
            ## Iterate over each column and consider any move by either side as the firstMove
            ## The move by the other side is then considered as the counterMove
            ## Here, our firstMove refers to AI's move and the opponent's move is considered as counterMove
            ## Take a deep copy of the board to prevent mutual influence between board and dupeBoard
            dupeBoard = copy.deepcopy(board)
            if not self.isValidMove(dupeBoard, firstMove):
            ## If the move of placing a black piece in the column specified by firstMove is invalid in dupeBoard
                continue
                ## Continue to the next firstMove
            self.makeMove(dupeBoard, tile, firstMove)
            ## If it is a valid move, set the corresponding grid color
            if self.cfw.doCheck(dupeBoard)==tile:
            ## If AI wins
                potentialMoves[firstMove] = 1
                ## The winning piece automatically gets a high value to indicate its chances of winning
                ## The larger the value, the higher the chances of winning, and the lower the chances of the opponent winning
                break
                ## Do not interfere with the calculation of other moves
            else:
                if self.cfw.isBoardFull(dupeBoard):
                ## If there are no empty grids in dupeBoard
                    potentialMoves[firstMove] = 0
                    ## It is not possible to move
                else:
                    for counterMove in range(len(board[0])):
                    ## Consider the opponent's move
                        dupeBoard2 = copy.deepcopy(dupeBoard)
                        if not self.isValidMove(dupeBoard2, counterMove):
                            continue
                        self.makeMove(dupeBoard2, enemyTile, counterMove)
                        if self.cfw.doCheck(dupeBoard2)== enemyTile:
                            potentialMoves[firstMove] = -1
                            ## If the player wins, the fitness value for AI in this column is the lowest
                            break
                        else:
                            ## Recursively call getPotentialMoves
                            results = self.getPotentialMoves(dupeBoard2, tile, lookAhead - 1)
                            ## Use floating-point representation here for more accurate results
                            ## This ensures that the values in potentialMoves are within the range [-1, 1]
                            potentialMoves[firstMove] += (sum(results)*1.0 / len(board[0])) / len(board[0])

        print("Potential Moves: "+str(potentialMoves))
        return potentialMoves


    def getComputerMove(self,board):
        potentialMoves = self.getPotentialMoves(board, self.cfw.figset[1],self.difficulty) ## Potential moves, a list with BOARDWIDTH values
                   ## The values in the list are related to the difficulty level set
        bestMoves = [] ## Create an empty bestMoves list
        bestMoveFitness = -1 ## Since the minimum value in potentialMoves is -1, it serves as the lower limit
        print(bestMoveFitness)
        for i in range(len(potentialMoves)):
            if potentialMoves[i] > bestMoveFitness and self.isValidMove(board, i):
                bestMoveFitness = potentialMoves[i] ## Continuously update bestMoves, so that each value in bestMoves is the largest
                ## while ensuring that the move is valid.

        for i in range(len(potentialMoves)):
            if potentialMoves[i] == bestMoveFitness and self.isValidMove(board, i):
                bestMoves.append(i) ## List all the columns where the piece can be moved to. This list may be empty, contain
                ## only one value, or multiple values.
        print(bestMoves)
        return random.choice(bestMoves) ## Randomly choose one of the columns where the piece can be moved to as the target move.
