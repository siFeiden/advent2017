import random as r


class Door(object):
  def __init__(self, title, done):
    self.title = title
    self.done = done

  @staticmethod
  def for_day(day):
    return Door('long ' * r.randint(2, 5), r.randint(0, 1))

