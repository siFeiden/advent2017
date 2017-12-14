def test(tested_mod, Assert):
  test_cases = [
    # (expected, inputs)
    (([], []), 0, 0, 1, 1, []),
    (([[3, 1]], []), 1, 1, 3, 4, [[3, 1]]),
    (([[0, 1], [2, 0]], [[4, 5]]), 0, 0, 4, 4, [[4, 5], [0, 1], [2, 0]])
  ]

  return Assert.all(tested_mod.bereiche, test_cases)

