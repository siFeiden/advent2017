import shutil

from os import path
from advent.door import Door


TEMPLATES_BASE_PATH = 'doors'
BASE_PATH = 'tuerchen'

class CopyNoOverwriteFile(object):
  def __init__(self, src, dest):
    self.src = src
    self.dest = dest

  def copy(self):
    if not path.exists(self.dest):
      shutil.copyfile(self.src, self.dest)

class CopyDoorFile(CopyNoOverwriteFile):
  def __init__(self, day):
    file_name = 'tuerchen{}.py'.format(day)
    door_file = path.join(BASE_PATH, file_name)

    template_name = 'door{}.py'.format(day)
    door_template = path.join(TEMPLATES_BASE_PATH, template_name)
    super().__init__(door_template, door_file)


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

