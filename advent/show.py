from advent.door import Door
from advent.doorio import CopyDoorFile


def present(day):
  CopyDoorFile(day).copy()

  door = Door.for_day(day)

  print(door.title)
  print()
  print(door.description)
  print()
  print()
  print('Löse dein Türchen in der Datei tuerchen/tuerchen{}.py.'.format(day))
  print('Dann starte `python advent.py test {}`, um deine Lösung zu testen :)'.format(day))

