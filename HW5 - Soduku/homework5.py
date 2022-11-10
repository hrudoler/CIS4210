############################################################
# CIS 521: Sudoku Homework 
############################################################

student_name = "Helen Rudoler"

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
import collections


############################################################
# Section 1: Sudoku Solver
############################################################

def sudoku_cells():
    return [(row, col) for row in range(9) for col in range(9)]

def sudoku_arcs():
    arcs = set()
    # gets cells in same row or column
    for first_row, first_col in sudoku_cells():
        for second_row, second_col in sudoku_cells():
            if ((first_row, first_col) != (second_row, second_col)):
                if (first_row == second_row or first_col == second_col):
                    arcs.add(((first_row, first_col), (second_row, second_col)))
                    arcs.add(((second_row, second_col), (first_row, first_col)))
                elif (first_row // 3 == second_row // 3 and first_col//3 == second_col // 3):
                    arcs.add(((first_row, first_col), (second_row, second_col)))
                    arcs.add(((second_row, second_col), (first_row, first_col)))
    return arcs
    

def read_board(path):
    board = {}
    f = open(path, 'r')
    row = 0
    for line in f:
        col = 0
        for char in line:
            if char.isdigit(): board[(row, col)] = {int(char)}
            elif char == "*": board[(row, col)] = {1, 2, 3, 4, 5, 6, 7, 8, 9}
            col += 1
        row += 1
    f.close()
    return board

            

class Sudoku(object):
    CELLS = sudoku_cells()
    ARCS = sudoku_arcs()

    def __init__(self, board):
        self.board = board


    def get_values(self, cell):
        return self.board[cell]

    def remove_inconsistent_values(self, cell1, cell2):
        revised = False
        inconsistant_values = set()
        for value in self.board[cell1]:
            if (cell1, cell2) in Sudoku.ARCS:
                if len(self.board[cell2]) == 1:
                    if value in self.board[cell2]:
                        # print(f"found inconsistant value {value} in {cell1} because of {cell2}")
                        inconsistant_values.add(value)
                        revised = True
        if revised:
            self.board[cell1] = {x for x in self.board[cell1] if x not in inconsistant_values}
            # print(f"removed inconsistant values: {inconsistant_values} from {cell1}")
        return revised


    def get_cell_arcs(self, cell):
        return {arc for arc in Sudoku.ARCS if arc[0] == cell}



    def infer_ac3(self):
        queue = collections.deque(Sudoku.ARCS)
        while queue:
            curr_arc = queue.pop()
            cell1 = curr_arc[0]
            cell2 = curr_arc[1]
            if len(self.board[cell1]) > 1 and self.remove_inconsistent_values(cell1, cell2):
                for next_arc in Sudoku.ARCS:
                    if (next_arc[0] == cell1 or next_arc[1] == cell1 and next_arc != curr_arc):
                        queue.append(next_arc)


    def unique_in_row(self, cell, value):
        for col in range(9):
            if col != cell[1] and value in self.board[(cell[0], col)]:
                return False
        return True

    def unique_in_col(self, cell, value):
        for row in range(9):
            if row != cell[0] and value in self.board[(row, cell[1])]:
                return False
        return True

    def unique_in_block(self, cell, value):
        row_block = cell[0] // 3
        col_block = cell[1] // 3
        for cell2 in Sudoku.CELLS:
            if cell2 != cell and cell2[0] // 3 == row_block and cell2[1] // 3 == col_block and value in self.board[cell2]:
                return False
        return True


    def infer_improved(self):
        made_additional_inference = True
        while made_additional_inference:
            self.infer_ac3()
            made_additional_inference = False
            for cell1 in Sudoku.CELLS:
                if (len(self.board[cell1]) > 1):
                    for value in self.board[cell1]:
                        if (self.unique_in_block(cell1, value) or self.unique_in_row(cell1, value) or self.unique_in_col(cell1, value)):
                            made_additional_inference = True
                            self.board[cell1] = {value}
                            break

    def copy_board(self):
        copy = {}
        for row in range(9):
            for col in range(9):
                copy[(row, col)] = self.board[(row, col)]
        return Sudoku(copy)

    def is_solved(self):
        for cell in Sudoku.CELLS:
            if len(self.board[cell]) > 1:
                return False
            for cell1, cell2 in Sudoku.ARCS:
                if cell == cell1:
                    if self.board[cell2] == self.board[cell]:
                        return False
        return True

    def infer_with_guessing(self):
        self.infer_improved()
        for cell in Sudoku.CELLS:
            if len(self.board[cell]) > 1:
                for value in self.board[cell]:
                    copy = self.copy_board()
                    copy.board[cell] = {value}
                    copy.infer_with_guessing()
                    if copy.is_solved():
                        self.board = copy.board
                        break

        
############################################################
# Section 2: Feedback
############################################################

# Just an approximation is fine.
feedback_question_1 = 8

feedback_question_2 = """
It took me a while to understand how to find the arcs in simple way. 
"""

feedback_question_3 = """
I liked the homework the way it was. 
"""
