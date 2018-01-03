def test(tested_mod, Assert):
  sudoku4x4f   = [[1,1,1,1]] * 4
  sudoku4x4ff  = [[3,4,1,2]] * 4
  sudoku4x4fff = [[1,2,3,4], [1,2,3,4], [1,2,3,4], [1,2,3,4]]
  sudoku4x4t   = [[3,4,1,2], [1,2,3,4], [4,3,2,1], [2,1,3,4]]

  test_cases = [
    # (expected, inputs)
    (False, sudoku4x4f),
    (False, sudoku4x4ff),
    (False, sudoku4x4fff),
    (True, sudoku4x4t),
  ]

  return Assert.all(tested_mod.auf_beiden, test_cases)
