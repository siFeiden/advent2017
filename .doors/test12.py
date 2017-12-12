def test(tested_mod, Assert):
  test_cases = [
    # (expected, inputs)
    (2, [[1, 1], [1, 3]]),
    (6, [[1, 1], [1, 4], [4, 4]]),
    (10, [[0, 0], [3, 4], [6, 0]])
  ]

  return Assert.all(tested_mod.streckenlaenge, test_cases)
