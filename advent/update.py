import shutil

from os import path
from urllib import request

from advent import doorio
from advent.door import Door


class HttpDownloadFile(object):
  def __init__(self, url, dest):
    self.url = url
    self.dest = dest

  def get(self):
    try:
      with request.urlopen(self.url) as dl:
        if dl.code == 200:
          with open(self.dest) as f:
            shutil.copyfileobj(dl, f)
            return True

        return False
    except:
      return False
    

class DoorLoader(HttpDownloadFile):
  # URL_TEMPLATE = 'http://raw.githubusercontent.com/siFeiden/advent/master/doors/door{}.py'
  URL_TEMPLATE = 'http://raw.githubusercontent.com/weltoph/buk-tools/master/Makefile'

  def __init__(self, day):
    url = self.URL_TEMPLATE.format(day)
    template_name = 'door{}.py'.format(day)
    dest = path.join(doorio.TEMPLATES_BASE_PATH, template_name)

    super().__init__(url, dest)


def load():
  # for day in range(1, 25):
  for day in range(1, 2):
    door = Door.for_day(day)
    if not door.is_loaded():
      print ('loading door', day)
      if not DoorLoader(day).get():
        break
  
