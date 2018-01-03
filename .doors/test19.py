def test(tested_mod, Assert):
  test_cases = [
    # (expected, inputs)
    (True, 7),
    (True, 23),
    (True, 997),
    (True, 2),
    (False, 4),
    (False, 15),
    (False, 998)
  ]

  return Assert.all(tested_mod.primzahl, test_cases)
