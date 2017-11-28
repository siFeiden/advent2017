from advent.doorio import DoorSuccessReader, DoorTemplateModuleLoader


class DoorInfoSplit(object):
  def __init__(self, text):
    self.text = text

  def split_title_description(self):
    lines = self.text.splitlines()
    title = lines[0]
    description = '\n'.join(lines[2:])

    return title, description


class Door(object):
  def __init__(self, day, module):
    self.day = day
    self.title, self.description = DoorInfoSplit(module.__doc__.strip()).split_title_description()
    self.done = DoorSuccessReader(day).read()

  @staticmethod
  def for_day(day):
    mod = DoorTemplateModuleLoader(day).load()
    return Door(day, mod)

