## Die Methoden dieser Klassen sind meist sehr lange, oftmals einige hundert Zeilen oder länger

Die Unix-Philosophie sagt: _Schreibe Computerprogramme so, dass sie nur eine Aufgabe erledigen und diese gut machen._
Rob Pike schrieb dazu: _Benutze sowohl einfache Algorithmen als auch einfache Datenstrukturen._ 

Große Klassen machen das Testen schwieriger und erhöhen die Abhängigkeiten. Es wird dadurch auch schwerer, Klassen bei Bedarf auszutauschen.
Ebenso, bei solchen gewachsenen Strukturen ist es nicht immer ersichtlich, was die Klasse bereits kann und inwiefern sie erweitert werden kann.

Reine Spekulation, aber es kann natürlich passieren, dass diese Klassen auch Dinge machen, die sie wahrscheinlich nicht sollten und könnten in kleinere Interfaces aufgeteilt werden.

In Summe ist das wahrscheinlich eine Anspielung auf das SOLID-Prinzip.

## spärlich dokumentiert

So etwas ist natürlich ein Klassiker. Wenn es wenige, komplexe Klassen mit wenig Dokumentation gibt, ist das schon einmal suboptimal für den Überblick. 

## Nachteile

Es wird am Anfang relativ schwierig sein, sich einen Überblick zu verschaffen. Praktisch wäre es natürlich, wenn es einige Skizzen gibt, wie diese Klassen miteinander interargieren. Das muss nicht unbedingt ein Klassendiagramm sein, sondern kann auch eine informale Grafik sein. 
Sollte nichts davon vorhanden sein, so müsste man sich damit beschäftigen, ob es zumindest Tests gibt, aus denen man ein Verhalten ableiten kann.
In jedem Fall bringt beides einen gewissen Mehraufwand mit sich, wenn das Projekt nicht ordentlich strukturiert ist.
Von der Beschreibung klingt es so, als ob die Klassen wahrscheinlich mehr als eine Sache machen und somit auch schwerer zu warten sind, das heißt, zu Beginn des Projektes wird eine zeitlang Arbeit nur in Refaktorierungen fließen, die Zeit und Nerven kosten.
Wenn das passiert ist kann langsam einmal mit dem Arbeiten begonnen werden, falls alles noch funktioniert (was nach dem Refaktorieren ja nicht uuuuunbedingt der Fall sein muss).
Zudem ist es relativ mühsam, wenn man sich die Dokumentation erst im Nachhinein dazudenken muss. Im besten Fall wird die Dokumentation vor dem Schreiben der Klasse geschrieben und definiert, was die Klasse oder Methode machen soll. Was sie macht sieht man ja ohenhin im Code.
