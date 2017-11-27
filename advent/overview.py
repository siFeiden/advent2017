import os

from . import dates
from .door import Door


TREE_WIDTH = 23
TREE_PADDING = 4

def show():
  with open('tree') as f:
    today = dates.today()

    row, cols = os.popen('stty size', 'r').read().split()
    window_width = int(cols)
    title_width = window_width - TREE_WIDTH - 2*TREE_PADDING

    for day, line in enumerate(f, start=1):
      if dates.check_day(day):
        door = Door.for_day(day)

        # Format: day number and door title
        t = '{:<2}  {}'.format(day, door.title).ljust(title_width)

        # Ellipsise if description is too long
        if len(t) > title_width:
          t = t[:title_width-2] + '..'

        # print line of tree only if door is done
        if door.done:
          print(t, ' '*TREE_PADDING, line.rstrip(), sep='')
        else:
          print(t)
      else:
        print(day)
