def test(tested_mod, Assert):
  test_cases = [
    (2, [2]),
    (2.5, [1,2,3,4]),
    (4, [4,4,4,4])
  ]

  return Assert.all(tested_mod.durchschnitt_geschenke, test_cases)
