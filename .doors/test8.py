def test(tested_mod, Assert):
  test_cases = [
    # (expected, inputs)
    (0, [['ja']]),
    (1, [['nein', 'ja'], ['ja', 'ja']]),
    (2, [['nein', 'nein', 'ja'], ['ja', 'nein', 'ja'], ['nein', 'ja', 'ja']]),
  ]

  return Assert.all(tested_mod.schlecht_behandelt, test_cases)
