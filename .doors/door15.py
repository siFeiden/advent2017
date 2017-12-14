"""
Tourenbereiche

Der Weihnachtsmann hat natuerlich einige helfende Haende wenn es
an die Auslieferung der Geschenke geht. Fuer jeden Helfer muss aber
auch eine Weihnachtsliefertour geplant werden. Das geht am einfachsten,
indem man jedem Helfer einen Bereich zuordnet und darin eine Tour plant.
Heute sollen die Bereiche geplant werden. Jeder Bereich wird über einen
Mittelpunkt definiert. Zwischen zwei benachbarten Bereichen muessen
jetzt die Haeuser aufgeteilt werden!
Dazu werden die Haeuser in der Umgebung einfach dem Mittelpunkt
zugeteilt, der am Naehesten liegt, zB
Mittelpunkt 1: (1, 1)
Mittelpunkt 2: (3, 4)
Haus: (3, 1)
Dann wird das Haus Mittelpunkt 1 zugeteilt, weil der Abstand am
geringsten ist.
"""

def bereiche(x1, y1, x2, y2, haeuser_liste):
  bereich1 = []
  bereich2 = []

  # Teile hier jedes Haus dem naeher gelegenen Mittelpunkt zu!
  # Mittelpunkt 1 hat die Koordinaten (x1, y1), Mittelpunkt 2
  # hat Koordinaten (x2, y2). Fuege die Koordinaten des Hauses
  # der Liste seines Bereichs hinzu.

  return bereich1, bereich2

