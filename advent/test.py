import random

from advent.doorio import DoorSuccessUpdate, DoorFile
from advent import dates


class Assert(object):
  def __init__(self, function):
    self.function = function
    self.ncases = 0
    self.npassed = 0
    self.failed = []

  def assert_true(self, expected, *args, **kwargs):
    self.ncases += 1

    actual = self.function(*args, **kwargs)

    if expected == actual:
      self.npassed += 1
    else:
      self.failed.append((expected, actual, args, kwargs))

  def passed_all(self):
    return self.npassed == self.ncases

  @property
  def nfailed(self):
    return len(self.failed)

  @classmethod
  def all(clazz, function, cases):
    t = clazz(function)
    for expected, *args in cases:
      t.assert_true(expected, *args)

    return t


class RandomCheer(object):
  def cheer(self):
    return random.choice(self.cheers)


class HappyCheer(RandomCheer):
  cheers = ['Wuhuu!', 'Yeah!', 'Yippie!', 'Yes!', 'Glückwunsch!',
            'Yihhaa!', 'Yaaaay!']


class SadCheer(RandomCheer):
  cheers = ['Noooo! :(', 'Neiiin! :(', 'Schade! :(', 'Och nöö! :(',
            'Mist! :(', 'Scheibenkleister :(']


@dates.nosy_wiebke_guard
def test(door):
  tester = door.test.module()
  tested_mod = door.solution.module()

  if tester is None:
    print('Huch, irgendwas ist schief gelaufen!')
    print('Ich kann das gerade nicht testen :(')
    print('Starte mal `python advent.py show {}`, vielleicht hilft das.'.format(door.day))
    return

  if tested_mod is None:
    print('Huch, es gibt noch gar keine Lösung zum Türchen {}!'.format(door.day))
    print('Starte `python advent.py show {}` um dir das Türchen anzeigen zu lassen :)'.format(door.day))
    return

  asserted = tester.test(tested_mod, Assert)

  if asserted.passed_all():
    DoorSuccessUpdate(door.day).update()
    print(HappyCheer().cheer(), '{0} / {0} Tests bestanden.'.format(asserted.npassed))
    print('Damit hast du das Türchen Nummer {} gelöst :)!'.format(door.day))
  else:
    print(SadCheer().cheer())
    print(asserted.nfailed, 'Tests nicht bestanden, da musst du nochmal ran!')
    print('Hier siehst du, was schief gegangen ist:')
    print()

    for i, (expected, actual, args, kwargs) in enumerate(asserted.failed):
      print('Test', i)
      print('  Eingabe:', *args)
      print('  Erwartete Ausgabe:', expected)
      print('  Deine Antwort:', actual)
      print()

    print('Versuchs nochmal :)')

