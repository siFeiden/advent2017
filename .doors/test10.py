def test(tested_mod, Assert):
  test_cases = [
    # (expected, inputs)
    ("Montag", 1),
    ("Dienstag", 2),
    ("Mittwoch", 3),
    ("Donnerstag", 4),
    ("Freitag", 5),
    ("Samstag", 6),
    ("Sonntag", 7)
  ]

  return Assert.all(tested_mod.tag_name, test_cases)
