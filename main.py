#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#############################################
# Author: Mario Schwaiger                   #
# Email: s54953@edu.campus02.at             #
# Created: 29.10.2024 17:50                 #
#############################################
__author__ = "Mario Schwaiger"
__credits__ = ["Mario Schwaiger","Andreas-Mihail Cojoc"]
__version__ = "0.1"
__maintainer__ = "Mario Schwaiger"
__email__ = "s54953@edu.campus02.at"
__status__ = "Development"

import sys
import numpy as np
import random, copy, pygame
import math
from pygame.locals import *
from viergewinnt.check_for_win import CheckForWin
from viergewinnt.ai import AIMoves
from viergewinnt.metagame import Metagame
from test.cmd_output import CMDOutput as cmdo

class Game(Metagame):
    ## Boldly stolen from: https://labex.io/tutorials/python-connect-four-game-human-vs-ai-298858

    DIFFICULTY = 2 ## Difficulty level, number of moves the computer can consider
                   ## Here, 2 means considering 7 possible moves of the opponent and how to respond to those 7 moves

    SPACESIZE = 50 ## Size of the chess pieces
    RADIUS = int(SPACESIZE/2 - 5)

    FPS = 30 ## Screen refresh rate, 30/s
    WINDOWWIDTH = 640  ## Width of the game screen in pixels
    WINDOWHEIGHT = 480 ## Height of the game screen in pixels

    BRIGHTBLUE = (0, 50, 255) ## Blue color
    WHITE = (255, 255, 255) ## White color

    BLUE = (0,0,255)
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    RED = (255,0,0)
    YELLOW = (255,255,0)

    BGCOLOR = BRIGHTBLUE
    TEXTCOLOR = WHITE

    WIN_WAIT_TIME=10000

    def __init__(self,rows,cols,wincnt,computer_game):

        self.turn=0

        self.cols=cols
        self.rows=rows
        self.wincnt=wincnt

        self.computer_game=computer_game
        
        self.XMARGIN = int((self.WINDOWWIDTH - self.cols * self.SPACESIZE) / 2)  ## X-coordinate of the left edge of the grid
        self.YMARGIN = int((self.WINDOWHEIGHT - self.rows * self.SPACESIZE) / 2) ## Y-coordinate of the top edge of the grid
        
        ## Initialize pygame modules
        pygame.init()

        ## Create a Clock object
        self.FPSCLOCK = pygame.time.Clock()

        ## Create the game window
        self.DISPLAYSURF = pygame.display.set_mode((self.SPACESIZE*self.cols, self.SPACESIZE*(self.rows+1)))

        ## Set the game window title
        pygame.display.set_caption(f'{self.wincnt} in row')

        ## Rect(left, top, width, height) is used to define position and size
        self.REDPILERECT = pygame.Rect(int(self.SPACESIZE / 2), self.WINDOWHEIGHT - int(3 * self.SPACESIZE / 2), self.SPACESIZE, self.SPACESIZE)

        ## Create the bottom left and bottom right chess pieces in the window
        self.BLACKPILERECT = pygame.Rect(self.WINDOWWIDTH - int(3 * self.SPACESIZE / 2), self.WINDOWHEIGHT - int(3 * self.SPACESIZE / 2), self.SPACESIZE, self.SPACESIZE)

        ## Load the red chess piece image
        self.REDTOKENIMG = pygame.image.load('images/4rowred.png')

        ## Scale the red chess piece image to SPACESIZE
        self.REDTOKENIMG = pygame.transform.smoothscale(self.REDTOKENIMG, (self.SPACESIZE, self.SPACESIZE))

        ## Load the black chess piece image
        self.BLACKTOKENIMG = pygame.image.load('images/4rowblack.png')

        ## Scale the black chess piece image to SPACESIZE
        self.BLACKTOKENIMG = pygame.transform.smoothscale(self.BLACKTOKENIMG, (self.SPACESIZE, self.SPACESIZE))

        ## Load the human winner image
        self.HUMANWINNERIMG ='images/4rowhumanwinner.png'

        ## Load the AI winner image
        self.COMPUTERWINNERIMG = 'images/4rowcomputerwinner.png'

        ## Load the tie image
        self.TIEWINNERIMG = 'images/4rowtie.jpg'

        self.myfont = pygame.font.SysFont("monospace", 75)

        self.board=self.create_board(self.cols,self.rows)

        self.cfw=CheckForWin(wincnt=self.wincnt, figset=self.FIGSET,reserved=self.RESERVED,drawretval=False)

        self.ai=AIMoves(self.cfw)


    def neues_fenster(self,image_path,text):
        pygame.display.set_mode((332, 332))  # Neues Fenster mit anderer Größe
        pygame.display.set_caption(text)
        screen = pygame.display.get_surface()
        screen.fill(self.WHITE)
        image=pygame.image.load(image_path)
        screen.blit(image, (0, 0))  # Bild in neues Fenster einfügen
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()    

   ## Stolen from: https://github.com/KeithGalli/Connect4-Python/blob/master/connect4.py
    def draw_board(self):
        
        for c in range(self.cols):
            for r in range(self.rows):
                pygame.draw.rect(self.DISPLAYSURF, self.BLUE, (c*self.SPACESIZE, r*self.SPACESIZE+self.SPACESIZE, self.SPACESIZE, self.SPACESIZE))
                pygame.draw.circle(self.DISPLAYSURF, self.BLACK, (int(c*self.SPACESIZE+self.SPACESIZE/2), int(r*self.SPACESIZE+self.SPACESIZE+self.SPACESIZE/2)), self.RADIUS)

        for c in range(self.cols):
            for r in range(self.rows):
                #self.YMARGIN-int(r*self.SPACESIZE+self.SPACESIZE/2))
                y_pos=int((self.SPACESIZE*self.rows)-r*self.SPACESIZE)
                x_pos=int(c*self.SPACESIZE)
                if self.board[r][c] == self.COIN_PLAYER_1:
                    self.DISPLAYSURF.blit(self.REDTOKENIMG,(x_pos,y_pos))
                    
                elif self.board[r][c] == self.COIN_PLAYER_2:
                    self.DISPLAYSURF.blit(self.BLACKTOKENIMG,(x_pos,y_pos))
                    
        pygame.display.update()  

                    
    def start(self):
        game_over=False
        turn=0
        fensterparameter={}
        while(not game_over):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(self.DISPLAYSURF, self.BLACK, (0,0, self.WINDOWWIDTH, self.SPACESIZE))
                    posx = event.pos[0]
                    if turn % 2 == 0:
                        #pygame.draw.circle(self.DISPLAYSURF, self.RED, (posx, int(self.SPACESIZE/2)), self.RADIUS)
                        self.DISPLAYSURF.blit(self.REDTOKENIMG,(posx,0))
                    else: 
                        #pygame.draw.circle(self.DISPLAYSURF, self.YELLOW, (posx, int(self.SPACESIZE/2)), self.RADIUS)
                        self.DISPLAYSURF.blit(self.BLACKTOKENIMG,(posx,0))
                pygame.display.update()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(self.DISPLAYSURF, self.BLACK, (0,0, self.XMARGIN, self.SPACESIZE))
                    #print(event.pos)
                    # Ask for Player 1 Input
                    #print(self.ai.getPotentialMoves(self.board,self.COIN_PLAYER_1,1))
                    if turn % 2 == 0:
                        posx = event.pos[0]
                        col = int(math.floor(posx/self.SPACESIZE))

                        #import ipdb; ipdb.set_trace()

                        if self.is_valid_location(self.board, col, self.rows):
                            row = self.get_next_open_row(self.board, col, self.rows)
                            self.drop_piece(row, col, self.COIN_PLAYER_1)

                            if self.cfw.doCheck(self.board)==self.COIN_PLAYER_1:
                                fensterparameter={"image_path":self.HUMANWINNERIMG,"text":"Spieler 1 gewinnt"}                            
                                game_over = True
                                #pygame.time.wait(self.WIN_WAIT_TIME)

                            if self.cfw.isBoardFull(self.board):
                                game_over=True
                                fensterparameter={"image_path":self.TIEWINNERIMG,"text":"Unentschieden"}
                                
                        if self.computer_game==1 and not game_over:
                            puttocol=self.ai.get_best_move(self.board,1)
                            row = self.get_next_open_row(self.board, puttocol, self.rows)
                            self.drop_piece(row, puttocol, self.COIN_PLAYER_2)
                            print(f"Droppend piece to:{row},{puttocol}")
                            turn+=1

                            if self.cfw.isBoardFull(self.board):
                                game_over=True
                                fensterparameter={"image_path":self.TIEWINNERIMG,"text":"Unentschieden"}

                    # # Ask for Player 2 Input
                    else:
                        posx = event.pos[0]
                        col = int(math.floor(posx/self.SPACESIZE))

                        if self.is_valid_location(self.board, col, self.rows):
                            row = self.get_next_open_row(self.board, col, self.rows)
                            self.drop_piece(row, col, self.COIN_PLAYER_2)

                    if self.cfw.doCheck(self.board)==self.COIN_PLAYER_2:
                        if self.computer_game==1:
                            fensterparameter={"image_path":self.COMPUTERWINNERIMG,"text":"Computergegner gewinnt"}
                        else:
                            fensterparameter={"image_path":self.COMPUTERWINNERIMG,"text":"Spieler 2 gewinnt"}

                        game_over = True
                        #pygame.time.wait(self.WIN_WAIT_TIME)

                    turn+=1
                    print(cmdo.doCMDOutput(self.board))
                    
                        #pygame.time.wait(self.WIN_WAIT_TIME)

                if game_over:
                    pygame.draw.rect(self.DISPLAYSURF, self.WHITE, (0,0, self.XMARGIN, self.SPACESIZE))
                    self.draw_board()
                    pygame.time.wait(self.WIN_WAIT_TIME)
                    self.neues_fenster(**fensterparameter)
                
                self.draw_board()

def main():
    # Standardwerte für 4 Gewinnt
    default_rows = 7
    default_cols = 6
    default_wincnt = 4
    computer_game = 1

    # Falls eine andere Brettgröße gewünscht ist als der Standard 
    try:
        rows = int(sys.argv[1]) if len(sys.argv) > 1 else default_rows
        cols = int(sys.argv[2]) if len(sys.argv) > 2 else default_cols
        wincnt=int(sys.argv[3]) if len(sys.argv) > 3 else default_wincnt
        computer_game=int(sys.argv[4]) if len(sys.argv) > 4 else computer_game
    except ValueError:
        print("Both rows, cols, and wincnt must be integers.")
        sys.exit(1)

    #assert rows >= wincnt and cols >= wincnt, f'Board must be at least {wincnt}x{wincnt}.'

    print(f"Rows: {rows}, Cols: {cols}, {wincnt} gewinnt")

    game = Game(rows,cols,wincnt,computer_game)
    game.start()
        

if __name__ == "__main__":
    main()
