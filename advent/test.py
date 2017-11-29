import random

from advent.doorio import DoorSuccessUpdate, DoorSolutionModuleLoader, DoorTesterModuleLoader


class RandomCheer(object):
  def cheer(self):
    return random.choice(self.cheers)


class HappyCheer(RandomCheer):
  cheers = ['Wuhuu!', 'Yeah!', 'Yippie!', 'Yes!', 'Glückwunsch!',
            'Yihhaa!', 'Yaaaay!']


class SadCheer(RandomCheer):
  cheers = ['Noooo! :(', 'Neiiin! :(', 'Schade! :(', 'Och nöö! :(',
            'Mist! :(', 'Scheibenkleister :(']


def test(day):
  tested_mod = DoorSolutionModuleLoader(day).load()
  tester = DoorTesterModuleLoader(day).load()

  if tester is None:
    print('Huch, irgendwas ist schief gelaufen!')
    print('Ich kann das gerade nicht testen :(')
    print('Starte mal `python advent.py update`.')
    # return

  if tested_mod is None:
    print('Huch, es gibt noch gar keine Lösung zum Türchen {}!'.format(day))
    print('Starte `python advent.py show {}` um dir das Türchen anzeigen zu lassen :)'.format(day))
    return

  if tester.test(tested_mod):
    DoorSuccessUpdate(day).update()
    print(HappyCheer().cheer())
    print('Tests bestanden, du hast das Türchen Nummer {} gelöst :)!'.format(day))
  else:
    print(SadCheer().cheer())
    print('Tests nicht bestanden, da musst du nochmal ran!')

