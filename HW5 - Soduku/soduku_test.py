import unittest
from homework5 import Sudoku, read_board, sudoku_arcs, sudoku_cells 

class TestSoduku(unittest.TestCase):
    def test_read_board_1(self):
        b = read_board("sudoku/medium1.txt")
        actual_vals = Sudoku(b).get_values((8, 8))
        expected_vals = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(actual_vals, expected_vals)
    
    def test_read_board_2(self):
        b = read_board("sudoku/medium1.txt")
        actual_vals = Sudoku(b).get_values((0, 1))
        expected_vals = set([1])
        self.assertEqual(actual_vals, expected_vals)

    def test_cells(self):
        c = sudoku_cells()
        self.assertEqual((8, 8), c[80])
    
    def test_arcs(self):
        a = sudoku_arcs()
        self.assertTrue(((0, 8), (0, 0)) in a)
        self.assertTrue(((0, 0), (1, 1)) in a)

    def test_remove_inconsistant(self):
        b = read_board("sudoku/medium1.txt")
        s = Sudoku(b)
        s.infer_ac3()

    def test_infer_improved(self):
        b = read_board("sudoku/medium1.txt")
        # print(f"all arcs: {Sudoku.ARCS}")
        s = Sudoku(b)
        s.infer_improved()
        # print(s.board)
        self.assertTrue(s.is_solved())
        

    def test_infer_guessing(self):
        b = read_board("sudoku/hard1.txt")
        s = Sudoku(b)
        s.infer_with_guessing()
        self.assertTrue(s.is_solved())
        print(s.board)



if __name__ == "__main__":
    unittest.main()