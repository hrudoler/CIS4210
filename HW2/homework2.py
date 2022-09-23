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
        b[row][col - 1] = not b[row][col - 1]
      if (row + 1 < self.m):
        b[row + 1][col] = not b[row + 1][col]
      if (col + 1 < self.n):
        b[row][col + 1] = not b[row][col + 1]

    def scramble(self):
      for row in range(self.m):
        for col in range(self.n):
          if random.random() < 0.5:
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
        state = self
        node = [[], state]
        if (state.is_solved()):
          return []
        frontier = collections.deque()
        frontier.append(node)
        tuple_node = tuple(map(tuple, self.board))
        reached = {tuple_node}

        while (len(frontier) > 0):
          node = frontier.popleft()
          all_moves = node[0]
          for child in node[1].successors():
            move = child[0]
            state = child[1]
            if (state.is_solved()):
              return all_moves + [move]
            tuple_child = tuple(map(tuple, state.board))
            if tuple_child not in reached:
              reached.add(tuple_child)
              frontier.append([all_moves + [move], state])
        return None

def create_puzzle(rows, cols):
    board = []
    for i in range(rows):
      a = []
      for j in range(cols):
        a.append(False)
      board.append(a)
    return LightsOutPuzzle(board)

############################################################
# Section 3: Linear Disk Movement
############################################################
def is_solved_indentical(board, n):
  end_filled = all(x for x in board[len(board) - n: len(board)])
  front_open = all(not x for x in board[:len(board) - n])
  return end_filled and front_open

def is_solved_distinct(board, n):
  counter = n
  for disk in board[len(board) - n: len(board)]:
    if disk != counter:
      return False
    counter -= 1
  front_open = all(not x for x in board[:len(board) - n])
  return front_open

def init_board_identical(length, n):
  front = [True] * n
  end = [False] * (length - n)
  return front + end

def init_board_distinct(length, n):
  front = [x + 1 for x in range(n)]
  end = [0] * (length - n)
  return front + end

def successors_identical(board):
  for index, disk in enumerate(board[:-1]):
    if disk:
      if not board[index + 1]:
        new_board = board.copy()
        new_board[index + 1] = True
        new_board[index] = False
        yield (index, index + 1), new_board
      elif index + 2 < len(board) and not board[index + 2]:
        new_board = board.copy()
        new_board[index + 2] = True
        new_board[index] = False
        yield (index, index + 2), new_board

def successors_distinct(board):
  for index, disk in enumerate(board[:-1]):
    if disk:
      new_board = board.copy()
      if not board[index + 1]:
        forward_val = new_board[index + 1]
        new_board[index + 1] = disk
        new_board[index] = forward_val
        yield (index, index + 1), new_board
      elif index + 2 < len(board) and not board[index + 2]:
        forward_val = new_board[index + 2]
        new_board[index + 2] = new_board[index]
        new_board[index] = forward_val
        yield (index, index + 2), new_board

def solve_identical_disks(length, n):
    state = init_board_identical(length, n)
    node = [[], state]
    if (is_solved_indentical(state, n)):
        return []
    frontier = collections.deque()
    frontier.append(node)
    while (len(frontier) > 0):
        node = frontier.popleft()
        all_moves = node[0]
        for child in successors_identical(node[1]):
            move = child[0]
            state = child[1]
            if (is_solved_indentical(state, n)):
                return all_moves + [move]
            frontier.append([all_moves + [move], state])
    return None

def solve_distinct_disks(length, n):
    state = init_board_distinct(length, n)
    node = [[], state]
    if (is_solved_distinct(state, n)):
      return []
    frontier = collections.deque()
    frontier.append(node)
    while (len(frontier) > 0):
        node = frontier.popleft()
        all_moves = node[0]
        for child in successors_distinct(node[1]):
          move = child[0]
          state = child[1]
          if (is_solved_distinct(state, n)):
            return all_moves + [move]
          frontier.append([all_moves + [move], state])
    return None

############################################################
# Section 4: Feedback
############################################################

feedback_question_1 = """
Approx 10 hours
"""

feedback_question_2 = """
Kept having a weird error with the light switching game, so I am really 
struggling to debug that. 
"""

feedback_question_3 = """
These games were REALLY satisfying once they worked! It's 
cool have these graph-search algos can solve these problems 
in such a methodical way. Very satisfying. 
"""