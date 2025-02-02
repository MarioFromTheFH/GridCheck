import logging

class CheckForWin():
    """
    Eine Klasse zur Überprüfung von Gewinnen in einem Spielraster.

    Attributes

    """

    def __init__(self, wincnt=4, figset=["x", "o"], reserved="0", drawretval=False):
        """
        Initialisiert die Klasse mit den erforderlichen Parametern.

        Parameters
        ----------
        wincnt : int, optional
            Anzahl der benötigten Steine in einer Reihe zum Gewinnen (default: 4).
        figset : list, optional
            Liste der gültigen Spielsteine (default: ["x", "o"]).
        reserved : str, optional
            Zeichen für ein leeres Feld (default: "0").
        drawretval : bool, optional
            Rückgabewert, falls kein Gewinner festgestellt wurde (default: False).
        """
        self.wincnt = wincnt
        self.figset = figset
        self.reserved = reserved
        self.drawretval = drawretval

        logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.WARNING, format="%(message)s")

    @property
    def figset(self):
        """
        Getter-Methode für figset.

        Returns
        -------
        list
            Liste der gültigen Spielsteine.
        """
        return self._figset

    @figset.setter
    def figset(self, figset):
        """
        Setter-Methode für figset.

        Parameters
        ----------
        figset : list
            Liste der gültigen Spielsteine.
        """
        self._figset = figset

    def doCheck(self, grid):
        """
        Überprüft das Spielfeld auf einen Gewinner.

        Parameters
        ----------
        grid : list of lists
            Das Spielfeld als 2D-Array.

        Returns
        -------
        str or bool
            Gibt den Gewinnerstein zurück oder False, wenn es keinen Gewinner gibt.
        """
        for method in (self.check_horizontally, self.check_vertically, self.check_diagonally):
            result = method(grid)
            if result is not False:
                return result
        return False

    def isBoardFull(self, grid):
        """
        Prüft, ob das Spielfeld vollständig belegt ist.

        Parameters
        ----------
        grid : list of lists
            Das Spielfeld als 2D-Array.

        Returns
        -------
        bool
            True, wenn das Spielfeld voll ist, sonst False.
        """
        for x in range(len(grid[0])):
            for y in range(len(grid)):
                if grid[y][x] == self.reserved:
                    return False
        return True

    def check_diagonally(self, grid):
        """
        Überprüft das Spielfeld auf einen diagonalen Gewinner.

        Parameters
        ----------
        grid : list of lists
            Das Spielfeld als 2D-Array.

        Returns
        -------
        str or bool
            Gibt den Gewinnerstein zurück oder drawretval, wenn es keinen gibt.
        """
        dcount = [self.reserved, 0]
        for x in range(len(grid[0])):
            for y in range(len(grid)):
                dcount = [self.reserved, 0]
                if grid[y][x] in self.figset:
                    dcount = [grid[y][x], 1]
                    dres = self.check_diag_line_positiv(grid, x, y, dcount)
                    if dres != self.drawretval:
                        return dres

                    dcount = [grid[y][x], 1]
                    dres = self.check_diag_line_negativ(grid, x, y, dcount)
                    if dres != self.drawretval:
                        return dres

        return self.drawretval

    def check_diag_line_negativ(self, grid, x, y, dcount):
        """
        Überprüft eine diagonale Linie in absteigender Richtung auf einen Sieg.

        Parameters
        ----------
        grid : list of lists
            Das Spielfeld als 2D-Array.
        x : int
            X-Koordinate des gefundenen Steins.
        y : int
            Y-Koordinate des gefundenen Steins.
        dcount : list
            Liste mit dem gefundenen Stein und der aktuellen Zählung.

        Returns
        -------
        str or bool
            Gibt den Gewinnerstein zurück oder drawretval, wenn es keinen gibt.
        """
        if x + (self.wincnt - 1) >= len(grid[0]) or y - (self.wincnt - 1) < 0:
            return self.drawretval

        for x_diag, y_diag in zip(range(x + 1, x + self.wincnt), range(y - 1, y - (self.wincnt), -1)):
            if grid[y_diag][x_diag] == dcount[0]:
                dcount[1] += 1
                if dcount[1] >= self.wincnt:
                    return dcount[0]
            else:
                return self.drawretval

    def check_diag_line_positiv(self, grid, x, y, dcount):
        """
        Überprüft eine diagonale Linie in aufsteigender Richtung auf einen Sieg.

        Parameters
        ----------
        grid : list of lists
            Das Spielfeld als 2D-Array.
        x : int
            X-Koordinate des gefundenen Steins.
        y : int
            Y-Koordinate des gefundenen Steins.
        dcount : list
            Liste mit dem gefundenen Stein und der aktuellen Zählung.

        Returns
        -------
        str or bool
            Gibt den Gewinnerstein zurück oder drawretval, wenn es keinen gibt.
        """
        if x + self.wincnt - 1 >= len(grid[0]) or y + self.wincnt - 1 >= len(grid):
            return self.drawretval

        for x_diag, y_diag in zip(range(x + 1, x + self.wincnt), range(y + 1, y + self.wincnt)):
            if grid[y_diag][x_diag] == dcount[0]:
                dcount[1] += 1
                if dcount[1] >= self.wincnt:
                    return dcount[0]

        return self.drawretval

    def check_vertically(self, grid):
        """
        Überprüft das Spielfeld auf einen vertikalen Gewinner.

        Parameters
        ----------
        grid : list of lists
            Das Spielfeld als 2D-Array.

        Returns
        -------
        str or bool
            Gibt den Gewinnerstein zurück oder drawretval, wenn es keinen gibt.
        """
        vcount = [self.reserved, 0]
        for y in range(len(grid[0])):
            vcount = [self.reserved, 0]
            for x in range(len(grid)):
                if grid[x][y] == self.reserved:
                    vcount = [self.reserved, 1]
                    continue
                elif grid[x][y] in self.figset:
                    if grid[x][y] == vcount[0]:
                        vcount[1] += 1
                        if vcount[1] >= self.wincnt:
                            return grid[x][y]
                    else:
                        vcount[0] = grid[x][y]
                        vcount[1] = 1
        return self.drawretval

    def check_horizontally(self, grid):
        """
        Überprüft das Spielfeld auf einen horizontalen Gewinner.

        Parameters
        ----------
        grid : list of lists
            Das Spielfeld als 2D-Array.

        Returns
        -------
        str or bool
            Gibt den Gewinnerstein zurück oder drawretval, wenn es keinen gibt.
        """
        hcount = [self.reserved, 0]
        for row in grid:
            hcount = [self.reserved, 0]
            for col in row:
                for coin in col:
                    if coin == self.reserved:
                        hcount = [self.reserved, 1]
                        continue
                    elif coin in self.figset:
                        if coin == hcount[0]:
                            hcount[1] += 1
                            if hcount[1] >= self.wincnt:
                                return coin
                        else:
                            hcount[0] = coin
                            hcount[1] = 1
        return self.drawretval
