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

def main():
    p = create_puzzle(2, 2)
    p.get_board()[0][0] = p.get_board()[0][0]
    #(p.get_board())

def num_placements_all(n):
    return math.comb(n**2, n)

def num_placements_one_per_row(n):
    return n**n

def n_queens_valid(board):
    used_cols = set()
    right_diags = set()
    left_diags = set()
    for row, col in enumerate(board):
        if col in used_cols:
          return False
        used_cols.add(col)
        if (row - col) in right_diags:
          return False
        right_diags.add(row - col)
        if (row + col) in left_diags:
          return False
        left_diags.add(row + col)
    return True

def n_queens_helper(n, board):
  for col in range(n):
    possible_board = board.copy()
    possible_board.append(col)
    if n_queens_valid(possible_board):
      yield possible_board

def n_queens_recurse(n, k, gen, all_sol):
    if k == n:
      all_sol += list(gen)
      return all_sol
    for sol in gen:
      next_gen = n_queens_helper(n, sol)
      n_queens_recurse(n, k + 1, next_gen, all_sol)
    return all_sol

def n_queens_solutions(n):
  gen = n_queens_helper(n, [])
  sols = n_queens_recurse(n, 1, gen, []) 
  return sols

############################################################
# Section 2: Lights Out
############################################################

class LightsOutPuzzle(object):

# note: m = rows, n  = cols

    def __init__(self, board):
      self.board = board
      self.m = len(board)
      self.n = len(board[0])

    def get_board(self):
      return self.board

    def perform_move(self, row, col):
      b = self.board
      b[row][col] = not b[row][col]
      if (row > 0):
        b[row - 1][col] = not b[row - 1][col]
      if (col > 0):
        b[row][col - 1] = not b[row - 1][col - 1]
      if (row + 1 < self.m):
        b[row + 1][col] = not b[row + 1][col]
      if (col + 1 < self.n):
        b[row][col + 1] = not b[row][col + 1]

    def scramble(self):
      for row in range(self.m):
        for col in range(self.n):
          if random.random() < 0.5:
            #print(f"flipping row {row} col {col}")
            self.perform_move(row, col)


    def is_solved(self):
      for row in range(self.m):
        for col in range(self.n):
          if self.board[row][col]:
            return False
      return True

    def copy(self):
      copy = create_puzzle(self.m, self.n)
      for row in range(self.m):
        for col in range(self.n):
          copy.board[row][col] = self.board[row][col]
      return copy

    def successors(self):
      for row in range(self.m):
        for col in range(self.n):
          y = self.copy()
          y.perform_move(row, col)
          yield (row, col), y

    #frontier entries: [[moves], [board_state]]
    def find_solution(self):
        node = [[], self]
        if (node[1].is_solved()):
          return node
        frontier = collections.deque()
        frontier.append(node)
        tuple_node = tuple(map(tuple, self.board))
        reached = {tuple_node}

        while (len(frontier) != 0):
          node = frontier.popleft()
          #child[0] is move tuple, child[1] is the new puzzle object
          for child in node[1].successors():
            node[0].append(child[0])
            node[1] = child[1]
            if (child[1].is_solved()):
              return node[0]
            tuple_child = tuple(map(tuple, child[1].board))
            if tuple_child not in reached:
              reached.add(tuple_child)
              frontier.appendleft(node)
        return

def create_puzzle(rows, cols):
    return LightsOutPuzzle([[True] * cols] * rows)

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