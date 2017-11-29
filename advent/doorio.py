from os import path

import importlib.util
import json
import shutil


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


class DoorModuleLoader(object):
  MODULE_NAME_PATTERN = 'door{}'
  SUBDIR = TEMPLATES_BASE_PATH

  def __init__(self, day):
    self.day = day

  def load(self):
    try:
      module_name = self.MODULE_NAME_PATTERN.format(self.day)
      file_name = path.join(self.SUBDIR, module_name + '.py')

      spec = importlib.util.spec_from_file_location(module_name, file_name)
      mod = importlib.util.module_from_spec(spec)
      spec.loader.exec_module(mod)
      return mod
    except Exception as e:
      return None


class DoorTemplateModuleLoader(DoorModuleLoader):
  MODULE_NAME_PATTERN = 'door{}'
  SUBDIR = TEMPLATES_BASE_PATH


class DoorSolutionModuleLoader(DoorModuleLoader):
  MODULE_NAME_PATTERN = 'tuerchen{}'
  SUBDIR = BASE_PATH


class DoorTesterModuleLoader(DoorModuleLoader):
  MODULE_NAME_PATTERN = 'test{}'
  SUBDIR = TEMPLATES_BASE_PATH

