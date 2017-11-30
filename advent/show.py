from advent.door import Door


def present(door):
  where = door.show()

  print(door.title)
  print()
  print(door.description)
  print()
  print()
  print('Löse dein Türchen in der Datei {}.'.format(where.file_path))
  print('Dann starte `python advent.py test {}`, um deine Lösung zu testen :)'.format(door.day))

