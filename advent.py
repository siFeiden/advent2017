import enum
import sys

from advent import dates
from advent import overview
from advent import show
from advent import test
from advent import update
from advent.door import Door


INVALID_DAY = -1


class Command(enum.Enum):
  Overview = 'overview'
  Show = 'show'
  Test = 'test'
  Update = 'update'
  Reset = 'reset'


class Overview(object):
  def __init__(self):
    pass

class Show(object):
  def __init__(self, day):
    pass

class Test(object):
  def __init__(self, day):
    pass


class InvalidArgs(Exception):
  pass

class DayCheckFailed(Exception):
  pass


def parse_args(args):
  nargs = len(args)
  if nargs <= 1:
    return INVALID_DAY, Command.Overview

  if nargs == 2:
    try:
      day = int(args[1])
      cmd = Command.Show
    except ValueError:
      day = dates.today()
      try:
        cmd = Command(args[1].lower())
      except:
        raise InvalidArgs()
  
  if nargs == 3:
    try:
      cmd = Command(args[1].lower())
      day = int(args[2])
    except:
      raise InvalidArgs()

  return day, cmd

def main():
  try:
    day, cmd = parse_args(sys.argv)

    if cmd == Command.Overview:
      overview.show()
      return

    door = Door.for_day(day)

    if cmd == Command.Show:
      show.present(door)
    elif cmd == Command.Test:
      test.test(door)
    elif cmd == Command.Update:
      update.load()
    elif cmd == Command.Reset:
      where = door.reset()
      print('Türchen {} wiederhergestellt!'.format(day))
      print('Das Türchen findest du wie vorher unter {} :)'.format(where.file_path))

  except InvalidArgs:
    print('usage')
  except DayCheckFailed:
    print('Na na na!\nNicht so neugierig, das ist noch nicht dran!')


if __name__ == '__main__':
  main()
