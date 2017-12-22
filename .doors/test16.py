def test(tested_mod, Assert):
  test_cases = [
    # (expected, inputs)
    ([], []),
    ([1, 3, 5, 6], [1, 3, 5, 6]),
    ([1], [1, 1, 1]),
    ([3, 1, 5, 2], [3, 1, 1, 5, 2, 2, 2])
  ]

  return Assert.all(tested_mod.loesche_doppelte, test_cases)
