from advent.door import Door
from advent import dates


@dates.nosy_wiebke_guard
def present(door):
  try:
    where = door.show()
      

    print(door.title)
    print()
    print(door.description)
    print()
    print()
    print('Loese dein Tuerchen in der Datei {}.'.format(where.file_path))
    print('Dann starte `python advent.py test {}`, um deine Loesung zu testen :)'.format(door.day))
  except Door.CouldNotLoad:
    print('Das Tuerchen kann gerade nicht gezeigt werden.')
    print('Es wurde noch nicht geladen und vielleicht ist die Internetverbindung gerade schlecht :(')
    print('Versuchs spaeter nochmal! :)')
    return

