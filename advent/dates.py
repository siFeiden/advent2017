import datetime


def today():
  date = datetime.datetime.today()
  return date.day


class DayCheckFailed(Exception):
  def __init__(self, day):
    self.day = day
    self.days_to_go = day - today()


def check_day(day):
  date = datetime.datetime.today()
  return date.month == 12 and date.day <= date.day


def nosy_wiebke_guard(fun):
  def guarded(door, *args):
    if check_day(door.day):
      return fun(door, *args)
    else:
      raise DayCheckFailed(door.day)

  return guarded

