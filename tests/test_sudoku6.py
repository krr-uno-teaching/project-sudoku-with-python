from .helper_4_6 import  TestSudoku46

INSTANCES = "./instances/txt"
SOLUTIONS = "./solutions/q04"

class TestSudoku(TestSudoku46):

    def test_sudoku(self):
        self.helper_test_sudoku(INSTANCES, SOLUTIONS, "sudoku6.py")
