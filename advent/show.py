from advent.door import Door


def present(day):
  door = Door.for_day(day)
  door.copy_door_file()

  print(door.title)
  print()
  print(door.description)
  print()
  print()
  print('Löse dein Türchen in der Datei tuerchen/tuerchen{}.py.'.format(day))
  print('Dann starte `python advent.py test {}`, um deine Lösung zu testen :)'.format(day))
