import enum
import sys

class Overview(object):
  def __init__(self):
    pass

class Show(object):
  def __init__(self, day):
    pass

class Check(object):
  def __init__(self, day):
    pass


class InvalidArgs(Exception):
  pass

class DayCheckFailed(Exception):
  pass

def today():
  # TODO: check for December
  return 8

def check_day(day):
  return day <= today()


def parse_args(args):
  nargs = len(args)
  if nargs <= 1:
    raise InvalidArgs()

  if nargs == 2:
    try:
      day = int(args[1])
      cmd = 'show'
    except ValueError:
      day = today()
      cmd = args[1]
  
  if nargs == 3:
    cmd = args[1]
    try:
      day = int(args[2])
    except ValueError:
      raise InvalidArgs()
    
  if not check_day(day):
    raise DayCheckFailed()

  return day, cmd

if __name__ == '__main__':
  try:
    day, cmd = parse_args(sys.argv)
    print('day', day)
    print('cmd', cmd)

    """
    door = doors[day]
    if cmd == 'show':
      door.show()
    elif cmd == 'check':
      door.check()
    """
  except InvalidArgs:
    print('usage')
  except DayCheckFailed:
    print('Na na na!\nNicht so neugierig, das ist noch nicht dran!')

