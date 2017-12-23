def test(tested_mod, Assert):
  test_cases = [
    # (expected, inputs)
    ([], []),
    ([6, 5, 2, 1], [1, 3, 5, 6]),
    ([1, 1, 1], [1, 1, 1]),
    ([2, 2, 2, 5, 1, 1, 3], [3, 1, 1, 5, 2, 2, 2])
  ]

  return Assert.all(tested_mod.therdegmu, test_cases)
