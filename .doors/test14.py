def test(tested_mod, Assert):
  
  class AgnosticTuple(object):
    """2-tuple that neglects ordering"""
    def __init__(self, a, b):
      self.a = a
      self.b = b

    def __eq__(self, o):
      oa, ob = o
      a = self.a
      b = self.b
      return (oa == a and ob == b) or (oa == b and ob == a)

    def __str__(self):
      return "({0}, {1}) oder ({1}, {0})".format(self.a, self.b)

    def __repr__(self):
      return str(self)

  test_cases = [
    # (expected, inputs)
    (AgnosticTuple(0, 1), [[1, 1], [1, 3]]),
    (AgnosticTuple(0, 1), [[1, 1], [2, 3], [4, 0]]),
    (AgnosticTuple(1, 2), [[4, 4], [1, 4], [2, 4]]),
    (AgnosticTuple(0, 2), [[6, 7], [0, 0], [3, 4]])
  ]

  return Assert.all(tested_mod.naeheste_haeuser, test_cases)
