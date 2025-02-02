# n Gewinnt

## Intro

Dies ist eien Implementierung des beliebten Spiels 4-Gewinnt mit ein paar Besonderheiten. Es ist möglich, das Spielfeld beliebig groß zu machen und mit beliebig vielen Steinen zum Gewinnen zu spielen. Im Hintergrund ist eine verschachtelte Liste die mit reservierten Zeichen gefüllt ist. Beide Spiele haben ihre eigenen Zeichen, die sie zum Spielen verwenden. Pygame mappt das Ganze dann auf eine Oberfläche, die schön aussieht. 

Der Algorithmus, der die Steine abzählt ist 100% Bio und selbst geschrieben. 

- Die Einbindung von Grafiken und die Einbindung der KI sind gestohlen von: https://labex.io/tutorials/python-connect-four-game-human-vs-ai-298858
- Die KI, eine Monte-Carlo-Simulation ist effektiv das hier: https://towardsdatascience.com/beating-connect-four-with-ai-b88b220ff0f0
- Nachdem das Spielfeld beliebig groß sein kann, wird eine Grafik dafür gerendert, die ist von hier: https://github.com/KeithGalli/Connect4-Python/blob/master/connect4.py

## Spielstart
Das Spiel startet man über die Kommandozeile mit bis zu vier Parameter:
```
python3.10 main.py 4 3 3 0
```

Der erste Parameter steht für die Anzahl der Zeilen.
Der zweite Parameter steht für die Anzahl der Spalten.
Der dritte Parameter gibt an, wie viele Steine notwendig sind, das Spiel zu gewinnen
Der vierte Parameter gibt an, ob man gegen einen Computergegner spielen möchte. 0=Spieler 2, 1=Computergegner

## Verwendete Pakete
```
pygame==2.1.2
```
