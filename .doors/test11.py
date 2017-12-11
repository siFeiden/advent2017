def test(tested_mod, Assert):
  test_cases = [
    # (expected, inputs)
    (2, 1, 1, 1, 3),
    (5, 0, 0, 3, 4),
    (13, -1, -1, 4, 11)
  ]

  return Assert.all(tested_mod.hausabstand, test_cases)
