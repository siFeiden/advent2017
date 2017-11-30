from advent.doorio import DoorType, DoorFile, DoorSuccessReader

from os import path
from advent import doorio


class DoorInfoSplit(object):
  def __init__(self, text):
    if text:
      self.text = text.strip()
    else:
      self.text = '\n'

  def split_title_description(self):
    lines = self.text.splitlines()
    title = lines[0]
    description = '\n'.join(lines[2:])

    return title, description


class Door(object):
  class CouldNotLoad(Exception):
    pass

  def __init__(self, day):
    self.day = day
    self.done = DoorSuccessReader(day).read()

    self.template = DoorFile(day, DoorType.Template)
    self.test = DoorFile(day, DoorType.Test)
    self.solution = DoorFile(day, DoorType.Solution)

    if self.template.exists():
      template_module = self.template.module()
      t, d = DoorInfoSplit(template_module.__doc__).split_title_description()
      self.title = t
      self.description = d
    else:
      self.title = ''
      self.description = ''

  def is_loaded(self):
    return self.template.exists() and self.test.exists()

  def load(self):
    url = 'http://raw.githubusercontent.com/weltoph/buk-tools/master/Makefile'
    template_url = url
    test_url = url
    template_loaded = self.template.load_from(template_url)
    test_loaded = self.test.load_from(test_url)
    return template_loaded and test_loaded

  def show(self):
    if not self.is_loaded():
      if not self.load():
        raise self.CouldNotLoad()

    self.template.copy_to(self.solution)
    return self.solution

  def reset(self):
    self.template.copy_to(self.solution, overwrite=True)
    return self.solution

  @staticmethod
  def for_day(day):
    return Door(day)

