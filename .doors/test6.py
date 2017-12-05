def test(tested_mod, Assert):
  test_cases = [
    # (expected, inputs)
    (1, [1]),
    (4, [1, 4, 4, 7]),
    (3, [3, 1, 9, 3]),
    (3, [9, 3, 3, 1]),
  ]

  return Assert.all(tested_mod.median_geschenke, test_cases)
