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
    print('Löse dein Türchen in der Datei {}.'.format(where.file_path))
    print('Dann starte `python advent.py test {}`, um deine Lösung zu testen :)'.format(door.day))
  except Door.CouldNotLoad:
    print('Das Türchen kann gerade nicht gezeigt werden.')
    print('Es wurde noch nicht geladen und vielleicht ist die Internetverbindung gerade schlecht :(')
    print('Versuchs später nochmal! :)')
    return

