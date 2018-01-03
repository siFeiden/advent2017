"""
Sudoku

Heute ist der letzte Tag vor Heiligabend, alles ist schon
vorbereitet und der Weihnachtsmann hat frei. An solchen Tagen
loest er gerne mal ein Sudoku.

Hilf ihm herauszufinden, ob er das Sudoku richtig geloest hat.
"""

def sudoku_richtig(sudoku):
  korrekt = True

  # Pruefe hier, ob sudoku korrekt geloest ist!
  # Ein Sudoku ist eine Liste von Listen: jede innere Liste
  # ist eine Zeile des Sudokus. Die aeussere Liste enthaelt
  # die Zeilen von oben nach unten, zB
  # [[1,2,3,4], [1,2,3,4], [1,2,3,4], [1,2,3,4]] ist das
  # falsch geloeste 4x4-Sudoku
  # 1 2|3 4
  # 1 2|3 4
  # -------
  # 1 2|3 4
  # 1 2|3 4

  return korrekt # Gib True oder False zurueck
