import enum
import sys

from advent import dates
from advent import overview
from advent import show
from advent import test
from advent.door import Door

USAGE = """
Usage:
  Run `python advent.py` to get an overview of all days

  Run `python advent.py show 2` to show the task for day 2.
      Change the number for other days ;)

  Run `python advent.py test 2` to test your solution for day 2.

  Run `python advent.py reset 2` to reset your solution for day 2.
      You probably don't need this :D
"""

INVALID_DAY = -1


class Command(enum.Enum):
  Overview = 'overview'
  Show = 'show'
  Test = 'test'
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
    elif cmd == Command.Reset:
      where = door.reset()
      print('Türchen {} wiederhergestellt!'.format(day))
      print('Das Türchen findest du wie vorher unter {} :)'.format(where.file_path))

  except InvalidArgs:
    print(USAGE)
  except dates.DayCheckFailed as e:
    print('Na na na!')
    print('Nicht so neugierig, das ist noch nicht dran!')
    print('Nur noch {} mal schlafen bis das dran ist :)'.format(e.days_to_go))


if __name__ == '__main__':
  main()
