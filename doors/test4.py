def test(tested_mod, Assert):
  test_cases = [
    # (expected, input)
    ([4], [4]),
    ([9,6], [6,9]),
    ([4,3,2,1], [4,3,2,1]),
    ([4,3,2,1], [1,2,3,4]),
    ([9,5,2,1], [1,5,2,9])
  ]

  return Assert.all(tested_mod.sortierte_zettel, test_cases)
