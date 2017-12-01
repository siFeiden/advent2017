def test(tested_mod, Assert):
  test_cases = [
    # (expected, inputs)
    ((1, 1), 1, 1, 2, -1, 1, 0),
    ((1, 2), -1, 1, 1, 2, -1, 0),
  ]

  return Assert.all(tested_mod.loese_lgs, test_cases)
