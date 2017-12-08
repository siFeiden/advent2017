def test(tested_mod, Assert):
  test_cases = [
    # (expected, inputs)
    (2, [2, 3]),
    (5, [1, 2, 4, 5, 6]),
    (7, [1, 9, 5, 7, 2])
  ]

  return Assert.all(tested_mod.zweitlaengster_zettel, test_cases)
