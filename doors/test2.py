def test(tested_mod, Assert):
  test_cases = [
    (4, [4]),
    (4, [1,2,3,4]),
    (4, [4,3,2,1]),
    (4, [1,4,2,3]),
    (4, [1,4,2,4]),
    (4, [4,4,4,4])
  ]

  return Assert.all(tested_mod.meiste_geschenke, test_cases)
