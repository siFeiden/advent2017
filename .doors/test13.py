def test(tested_mod, Assert):
  test_cases = [
    # (expected, inputs)
    (0, 0, 0, [[1, 1], [1, 3]]),
    (1, 1, 1, [[4, 4], [1, 4], [2, 4]]),
    (2, 0, 1, [[6, 7], [3, 4], [0, 0]])
  ]

  return Assert.all(tested_mod.naehestes_haus, test_cases)
