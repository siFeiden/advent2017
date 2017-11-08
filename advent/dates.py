import datetime


def today():
  date = datetime.datetime.today()
  # TODO: check for December
  return date.day

def check_day(day):
  return day <= today()
