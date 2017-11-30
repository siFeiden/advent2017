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
    self.template.load_from(template_url)
    self.test.load_from(test_url)

  def show(self):
    self.template.copy_to(self.solution)
    return self.solution

  @staticmethod
  def for_day(day):
    return Door(day)

