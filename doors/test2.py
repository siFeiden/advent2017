def test(tested_mod, Assert):
  test_cases = [
    (4, 2, 2),
    (0, 0, 0),
    (7, 3, 4)
  ]

  return Assert.all(tested_mod.add_two, test_cases)
