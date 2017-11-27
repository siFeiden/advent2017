import importlib.util
import json
from os import path


BASE_PATH = 'doors'


class DoorInfoSplit(object):
  def __init__(self, text):
    self.text = text

  def split_title_description(self):
    lines = self.text.splitlines()
    title = lines[0]
    description = '\n'.join(lines[2:])

    return title, description


class DoorStatReader(object):
  def __init__(self, day):
    self.day = day

  def read(self):
    p = path.join(BASE_PATH, 'stat.json')
    with open(p) as f:
      stat = json.load(f)
      return stat['fns'][self.day - 1]

    return False


class Door(object):
  def __init__(self, day, module, file_name):
    self.day = day
    self.title, self.description = DoorInfoSplit(module.__doc__.strip()).split_title_description()
    self.done = DoorStatReader(day).read()

  @staticmethod
  def for_day(day):
    module_name = 'door{}'.format(day)
    file_name = path.join(BASE_PATH, module_name + '.py')

    spec = importlib.util.spec_from_file_location(module_name, file_name)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    return Door(day, mod, file_name)

