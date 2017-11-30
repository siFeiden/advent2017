import enum
import importlib.util
import json
import shutil

from os import path
from urllib import request


TEMPLATES_BASE_PATH = 'doors'
BASE_PATH = 'tuerchen'


class DoorType(enum.Enum):
  Template = 'doors/door{}.py'
  Test = 'doors/test{}.py'
  Solution = 'tuerchen/tuerchen{}.py'

  RemoteTemplate = 'https://raw.githubusercontent.com/siFeiden/advent2017/master/doors/door{}.py'
  RemoteTest = 'https://raw.githubusercontent.com/siFeiden/advent2017/master/doors/test{}.py'


class DoorSuccessReader(object):
  def __init__(self, day):
    self.day = day

  def read(self):
    p = path.join(TEMPLATES_BASE_PATH, 'stat.json')
    with open(p) as f:
      stat = json.load(f)
      return stat['fns'][self.day - 1]

    return False


class DoorSuccessUpdate(object):
  def __init__(self, day):
    self.day = day

  def update(self):
    p = path.join(TEMPLATES_BASE_PATH, 'stat.json')
    with open(p) as f:
      stat = json.load(f)
      stat['fns'][self.day - 1] = True

    with open(p, 'w') as f:
      json.dump(stat, f)


class HttpDownloadFile(object):
  def __init__(self, url, dest):
    self.url = url
    self.dest = dest

  def get(self):
    try:
      with request.urlopen(self.url.file_path) as dl:
        if dl.code == 200:
          with open(self.dest.file_path, 'wb') as f:
            shutil.copyfileobj(dl, f)
            return True

        return False
    except Exception as e:
      return False


class DoorFile(object):
  def __init__(self, day, door_type):
    self.day = day
    self.door_type = door_type
    self.file_path = door_type.value.format(day)
    self._module = None

  def exists(self):
    return path.exists(self.file_path)

  def load_from(self, remote_file):
    return HttpDownloadFile(remote_file, self).get()

  def copy_to(self, dest, overwrite=False):
    if overwrite or (not dest.exists()):
      shutil.copyfile(self.file_path, dest.file_path)
    
  def module(self):
    if self._module:
      return self._module

    try:
      module_name = self.door_type.name.lower() + str(self.day)

      spec = importlib.util.spec_from_file_location(module_name, self.file_path)
      mod = importlib.util.module_from_spec(spec)
      spec.loader.exec_module(mod)

      self._module = mod
      return mod
    except SyntaxError as se:
      raise se
    except IOError as e:
      return None

