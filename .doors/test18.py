def test(tested_mod, Assert):
  test_cases = [
    # (expected, inputs)
    ([], [], []),
    ([], [], ["Anne"]),
    ([], ["John"], ["John", "Anne"]),
    (["Hans", "Susi"], ["Hans", "Susi"], []),
    (["Peter"], ["Peter"], ["Kaya"]),
    (["Lena"], ["David", "Lena"], ["David", "Lisa"]),
  ]

  return Assert.all(tested_mod.streichen, test_cases)
