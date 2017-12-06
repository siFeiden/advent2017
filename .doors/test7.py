def test(tested_mod, Assert):
  test_cases = [
    # (expected, inputs)
    ((0, 0, 0), []),
    ((3, 0, 0), ['ja', 'ja', 'ja']),
    ((0, 2, 0), ['nein', 'nein']),
    ((2, 1, 1), ['ja', 'nein', 'ja', 'vielleicht']),
  ]

  return Assert.all(tested_mod.auswertung_umfrage, test_cases)
