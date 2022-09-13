############################################################
# CIS 521: Uninformed Search Homework
############################################################

student_name = "Helen Rudoler"

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
import math
import random
import itertools
import collections


############################################################
# Section 1: N-Queens
############################################################

def num_placements_all(n):
    math.comb(n**2, n)

def num_placements_one_per_row(n):
    return math.factorial(n - 1)

def n_queens_valid(board):
    n = len(board)
    used_spots = {}
    for index, col in board:
        if index not in used_spots:
            used_spots[index] = []
        if col in used_spots[index]:
            return False
        used_spots[index] = used_spots[index].append(col)
        


def n_queens_solutions(n):
    pass

############################################################
# Section 2: Lights Out
############################################################

class LightsOutPuzzle(object):

    def __init__(self, board):
        self.board = board
        self.m = len(board)
        self.n = len(board[0])

    def get_board(self):
        return self.board

    def perform_move(self, row, col):
        pass

    def scramble(self):
        pass

    def is_solved(self):
        pass

    def copy(self):
        pass

    def successors(self):
        pass

    def find_solution(self):
        pass

def create_puzzle(rows, cols):
    return [[False] * rows] * cols

############################################################
# Section 3: Linear Disk Movement
############################################################

def solve_identical_disks(length, n):
    pass

def solve_distinct_disks(length, n):
    pass

############################################################
# Section 4: Feedback
############################################################

feedback_question_1 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""

feedback_question_2 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""

feedback_question_3 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""
