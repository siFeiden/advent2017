import random

from advent.doorio import DoorSuccessUpdate, DoorFile


class RandomCheer(object):
  def cheer(self):
    return random.choice(self.cheers)


class HappyCheer(RandomCheer):
  cheers = ['Wuhuu!', 'Yeah!', 'Yippie!', 'Yes!', 'Glückwunsch!',
            'Yihhaa!', 'Yaaaay!']


class SadCheer(RandomCheer):
  cheers = ['Noooo! :(', 'Neiiin! :(', 'Schade! :(', 'Och nöö! :(',
            'Mist! :(', 'Scheibenkleister :(']


def test(door):
  tester = door.test.module()
  tested_mod = door.solution.module()

  if tester is None:
    print('Huch, irgendwas ist schief gelaufen!')
    print('Ich kann das gerade nicht testen :(')
    print('Starte mal `python advent.py update`.')
    # return

  if tested_mod is None:
    print('Huch, es gibt noch gar keine Lösung zum Türchen {}!'.format(door.day))
    print('Starte `python advent.py show {}` um dir das Türchen anzeigen zu lassen :)'.format(door.day))
    return

  if tester.test(tested_mod):
    DoorSuccessUpdate(door.day).update()
    print(HappyCheer().cheer())
    print('Tests bestanden, du hast das Türchen Nummer {} gelöst :)!'.format(door.day))
  else:
    print(SadCheer().cheer())
    print('Tests nicht bestanden, da musst du nochmal ran!')

