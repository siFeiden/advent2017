def test(tested_mod, Assert):
  test_cases = [
    (0, []),
    (4, [4]),
    (6, [1,2,3]),
    (45, [1,2,3,4,5,6,7,8,9])
  ]

  return Assert.all(tested_mod.anzahl_geschenke, test_cases)
