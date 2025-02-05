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
import random, copy, pygame
import math
from pygame.locals import *
from viergewinnt.check_for_win import CheckForWin
from viergewinnt.ai import AIMoves
from viergewinnt.metagame import Metagame
from test.cmd_output import CMDOutput as cmdo

class Game(Metagame):
    """
    Eine Klasse, die das Spiel "Vier Gewinnt" für einen menschlichen Spieler gegen den Computer implementiert.

    Sie erbt von der Metagame-Klasse und definiert wichtige Parameter wie die Spielfeldgröße,
    die Spielbildschirmgröße und den Schwierigkeitsgrad des Computers.
    """
    ## Ganz gemein gestohlen von: https://labex.io/tutorials/python-connect-four-game-human-vs-ai-298858

    DIFFICULTY = 2  ## Schwierigkeitsgrad, Anzahl der Züge, die der Computer berücksichtigen kann
                   ## Hier bedeutet 2, dass der Computer 7 mögliche Züge des Gegners berücksichtigt und darauf reagiert.

    SPACESIZE = 50  ## Größe der Spielfiguren in Pixeln
    RADIUS = int(SPACESIZE / 2 - 5)  ## Radius der Spielfigur (um den Mittelpunkt herum)

    WINDOWWIDTH = 640  ## Breite des Spielbildschirms in Pixeln
    WINDOWHEIGHT = 480  ## Höhe des Spielbildschirms in Pixeln

    BRIGHTBLUE = (0, 50, 255)  ## Helle Blautönung (RGB-Werte)
    WHITE = (255, 255, 255)  ## Weiß (RGB-Werte)

    BLUE = (0, 0, 255)  ## Blau (RGB-Werte)
    BLACK = (0, 0, 0)  ## Schwarz (RGB-Werte)
    WHITE = (255, 255, 255)  ## Weiß (RGB-Werte)

    WIN_WAIT_TIME = 10000  ## Wartezeit nach einem Gewinn in Millisekunden (10 Sekunden)

    def __init__(self, rows, cols, wincnt, computer_game):
        """
        Initialisiert das Spiel mit den angegebenen Parametern.

        Parameter
        ----------
        rows : int
            Die Anzahl der Zeilen auf dem Spielfeld.
        cols : int
            Die Anzahl der Spalten auf dem Spielfeld.
        wincnt : int
            Die Anzahl der Steine in einer Reihe, um zu gewinnen.
        computer_game : int
            1, wenn es sich um ein Spiel gegen den Computer handelt, andernfalls 0.
        """
        self.turn = 0
        self.cols = cols
        self.rows = rows
        self.wincnt = wincnt
        self.computer_game = computer_game

        # Berechnung der Margen für die X- und Y-Koordinaten
        self.XMARGIN = int((self.WINDOWWIDTH - self.cols * self.SPACESIZE) / 2)
        self.YMARGIN = int((self.WINDOWHEIGHT - self.rows * self.SPACESIZE) / 2)

        # Initialisiere pygame-Module
        pygame.init()

        # Erstelle das Spiel-Fenster
        self.DISPLAYSURF = pygame.display.set_mode((self.SPACESIZE * self.cols, self.SPACESIZE * (self.rows + 1)))

        # Setze den Titel des Fensters
        pygame.display.set_caption(f'{self.wincnt} in Reihe')

        # Definiere Rechtecke für die Spielfiguren
        self.REDPILERECT = pygame.Rect(int(self.SPACESIZE / 2), self.WINDOWHEIGHT - int(3 * self.SPACESIZE / 2),
                                       self.SPACESIZE, self.SPACESIZE)
        self.BLACKPILERECT = pygame.Rect(self.WINDOWWIDTH - int(3 * self.SPACESIZE / 2),
                                         self.WINDOWHEIGHT - int(3 * self.SPACESIZE / 2), self.SPACESIZE,
                                         self.SPACESIZE)

        # Lade die Bilder für die Spielfiguren
        self.REDTOKENIMG = pygame.image.load('images/4rowred.png')
        self.REDTOKENIMG = pygame.transform.smoothscale(self.REDTOKENIMG, (self.SPACESIZE, self.SPACESIZE))

        self.BLACKTOKENIMG = pygame.image.load('images/4rowblack.png')
        self.BLACKTOKENIMG = pygame.transform.smoothscale(self.BLACKTOKENIMG, (self.SPACESIZE, self.SPACESIZE))

        # Lade Bilder für Gewinner und Unentschieden
        self.HUMANWINNERIMG = 'images/4rowhumanwinner.png'
        self.COMPUTERWINNERIMG = 'images/4rowcomputerwinner.png'
        self.TIEWINNERIMG = 'images/4rowtie.jpg'

        # Erstelle das Spielfeld
        self.board = self.create_board(self.cols, self.rows)

        # Initialisiere die Gewinnprüfungs-Logik und die KI
        self.cfw = CheckForWin(wincnt=self.wincnt, figset=self.FIGSET, reserved=self.RESERVED, drawretval=False)
        self.ai = AIMoves(self.cfw)

    def neues_fenster(self, image_path, text):
        """
        Erstelle ein neues Fenster und zeige ein Bild und Text an.

        Parameter
        ----------
        image_path : str
            Der Pfad zum Bild, das angezeigt werden soll.
        text : str
            Der Text, der im Fenster angezeigt wird.
        """
        pygame.display.set_mode((332, 332))  # Neues Fenster mit einer anderen Größe
        pygame.display.set_caption(text)
        screen = pygame.display.get_surface()
        screen.fill(self.WHITE)
        image = pygame.image.load(image_path)
        screen.blit(image, (0, 0))  # Bild im neuen Fenster einfügen
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    def draw_board(self):
        """
        Zeichnet das Spielfeld und die Spielfiguren.

        Diese Methode zeichnet das Spielfeld basierend auf den aktuellen Spielständen
        und platziert die Spielfiguren an den richtigen Positionen.
        """
        for c in range(self.cols):
            for r in range(self.rows):
                pygame.draw.rect(self.DISPLAYSURF, self.BLUE, (
                c * self.SPACESIZE, r * self.SPACESIZE + self.SPACESIZE, self.SPACESIZE, self.SPACESIZE))
                pygame.draw.circle(self.DISPLAYSURF, self.BLACK, (int(c * self.SPACESIZE + self.SPACESIZE / 2),
                                                                  int(r * self.SPACESIZE + self.SPACESIZE + self.SPACESIZE / 2)),
                                   self.RADIUS)

        for c in range(self.cols):
            for r in range(self.rows):
                y_pos = int((self.SPACESIZE * self.rows) - r * self.SPACESIZE)
                x_pos = int(c * self.SPACESIZE)
                if self.board[r][c] == self.COIN_PLAYER_1:
                    self.DISPLAYSURF.blit(self.REDTOKENIMG, (x_pos, y_pos))
                elif self.board[r][c] == self.COIN_PLAYER_2:
                    self.DISPLAYSURF.blit(self.BLACKTOKENIMG, (x_pos, y_pos))

        pygame.display.update()

    def start(self):
        """
        Startet das Spiel und verarbeitet alle Benutzerinteraktionen.

        Diese Methode startet das Spiel, verarbeitet die Eingaben der Spieler
        und überprüft nach jedem Zug, ob das Spiel zu Ende ist.
        """
        game_over = False
        turn = 0
        fensterparameter = {}

        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(self.DISPLAYSURF, self.BLACK, (0, 0, self.WINDOWWIDTH, self.SPACESIZE))
                    posx = event.pos[0]
                    if turn % 2 == 0:
                        self.DISPLAYSURF.blit(self.REDTOKENIMG, (posx, 0))
                    else:
                        self.DISPLAYSURF.blit(self.BLACKTOKENIMG, (posx, 0))
                pygame.display.update()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(self.DISPLAYSURF, self.BLACK, (0, 0, self.XMARGIN, self.SPACESIZE))

                    # Spieler 1 Input
                    if turn % 2 == 0:
                        posx = event.pos[0]
                        col = int(math.floor(posx / self.SPACESIZE))

                        if self.is_valid_location(self.board, col, self.rows):
                            row = self.get_next_open_row(self.board, col, self.rows)
                            self.drop_piece(row, col, self.COIN_PLAYER_1)

                            if self.cfw.doCheck(self.board) == self.COIN_PLAYER_1:
                                fensterparameter = {"image_path": self.HUMANWINNERIMG, "text": "Spieler 1 gewinnt"}
                                game_over = True

                            if self.cfw.isBoardFull(self.board):
                                game_over = True
                                fensterparameter = {"image_path": self.TIEWINNERIMG, "text": "Unentschieden"}

                        else:
                            continue

                        if self.computer_game == 1 and not game_over:
                            puttocol = self.ai.get_best_move(self.board, 1)
                            row = self.get_next_open_row(self.board, puttocol, self.rows)
                            self.drop_piece(row, puttocol, self.COIN_PLAYER_2)
                            turn += 1

                            if self.cfw.isBoardFull(self.board):
                                game_over = True
                                fensterparameter = {"image_path": self.TIEWINNERIMG, "text": "Unentschieden"}

                    # Spieler 2 Input
                    else:
                        posx = event.pos[0]
                        col = int(math.floor(posx / self.SPACESIZE))

                        if self.is_valid_location(self.board, col, self.rows):
                            row = self.get_next_open_row(self.board, col, self.rows)
                            self.drop_piece(row, col, self.COIN_PLAYER_2)

                            if self.cfw.isBoardFull(self.board):
                                game_over = True
                                fensterparameter = {"image_path": self.TIEWINNERIMG, "text": "Unentschieden"}

                        else:
                            continue

                    if self.cfw.doCheck(self.board) == self.COIN_PLAYER_2:
                        if self.computer_game == 1:
                            fensterparameter = {"image_path": self.COMPUTERWINNERIMG, "text": "Computergegner gewinnt"}
                        else:
                            fensterparameter = {"image_path": self.COMPUTERWINNERIMG, "text": "Spieler 2 gewinnt"}

                        game_over = True

                    turn += 1

                if game_over:
                    pygame.draw.rect(self.DISPLAYSURF, self.WHITE, (0, 0, self.XMARGIN, self.SPACESIZE))
                    my_font = pygame.font.SysFont('Comic Sans MS', 30)
                    text_surface = my_font.render(fensterparameter["text"], False, (0, 0, 0))
                    self.DISPLAYSURF.blit(text_surface, (0, 0))
                    self.draw_board()
                    pygame.time.wait(self.WIN_WAIT_TIME)
                    self.neues_fenster(**fensterparameter)

                self.draw_board()


def main():
    """
    Der Einstiegspunkt des Programms, der das Spiel startet.

    Initialisiert das Spiel mit den Standardwerten oder den vom Benutzer
    angegebenen Parametern und startet es.
    """
    # Standardwerte für 4 Gewinnt
    default_rows = 7
    default_cols = 6
    default_wincnt = 4
    computer_game = 1

    # Falls eine andere Brettgröße gewünscht ist als der Standard
    try:
        rows = int(sys.argv[1]) if len(sys.argv) > 1 else default_rows
        cols = int(sys.argv[2]) if len(sys.argv) > 2 else default_cols
        wincnt = int(sys.argv[3]) if len(sys.argv) > 3 else default_wincnt
        computer_game = int(sys.argv[4]) if len(sys.argv) > 4 else computer_game
    except ValueError:
        print("Alle Eingabewerte müssen ganze Zahlen sein.")
        sys.exit(1)

    print(f"Reihen: {rows}, Spalten: {cols}, {wincnt} in Reihe")

    game = Game(rows, cols, wincnt, computer_game)
    game.start()


if __name__ == "__main__":
    main()
