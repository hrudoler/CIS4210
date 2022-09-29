############################################################
# CIS 521: Informed Search Homework
############################################################

student_name = "Helen Rudoler"

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
from queue import PriorityQueue
import math

############################################################
# Section 1: Tile Puzzle
############################################################

def create_tile_puzzle(rows, cols):
    outer_list = []
    tile_num = 1
    for _ in range(rows):
        inner_list = []
        for _ in range(cols):
            inner_list.append(tile_num)
            tile_num += 1
        outer_list.append(inner_list)
    outer_list[rows - 1][cols - 1] = 0
    return TilePuzzle(outer_list)

class TilePuzzle(object):
    # Required
    def __init__(self, board):
        self.board = board
        self.m = len(board)
        self.n = len(board[0])
        self.zero_location = (0,0)
        for row in range(self.m):
          for col in range(self.n):
            if board[row][col] == 0:
              self.zero_location = (row, col)
              break

    def get_board(self):
        return self.board

    def perform_move(self, direction):
        row = self.zero_location[0]
        col = self.zero_location[1]
        if direction == "up":
          if row > 0:
            new_row = row - 1
            self.zero_location = (new_row, col)
            self.board[row][col] = self.board[new_row][col]
            self.board[new_row][col] = 0
          return row > 0
        elif direction == "down":
          if row < (self.m - 1):
            new_row = row + 1
            self.zero_location = (new_row, col)
            self.board[row][col] = self.board[new_row][col]
            self.board[new_row][col] = 0
          return row < (self.m - 1)
        elif direction == "left":
          if col > 0:
            new_col = col - 1 
            self.zero_location = (row, new_col)
            self.board[row][col] = self.board[row][new_col]
            self.board[row][new_col] = 0
          return col > 0
        elif direction == "right":
          if col < (self.n - 1):
            new_col = col + 1 
            self.zero_location = (row, new_col)
            self.board[row][col] = self.board[row][new_col]
            self.board[row][new_col] = 0
          return col < (self.n - 1)
        return False

    def scramble(self, num_moves):
        pass

    def is_solved(self):
        return self.board == create_tile_puzzle(self.m, self.n).board

    def copy(self):
      copy = create_tile_puzzle(self.m, self.n)
      copy.zero_location = self.zero_location
      for row in range(self.m):
        for col in range(self.n):
          copy.board[row][col] = self.board[row][col]
      return copy

    def successors(self):
        allowed_moves = ['up', 'down', 'left', 'right']
        for move in allowed_moves:
          y = self.copy()
          move_is_valid = y.perform_move(move)
          if move_is_valid:
            yield move, y

    def iddfs_recurse(self, limit, moves):
        if limit <= 0:
          return
        limit -= 1
        for successor in self.successors():
          puzzle = successor[1]
          move = successor[0]
          if puzzle.is_solved():
            yield moves + [move], puzzle
          else:
            for next_node in puzzle.iddfs_recurse(limit, moves + [move]):
              yield next_node
            
    # Required
    def find_solutions_iddfs(self):
        depth = 0
        solved = False
        if self.is_solved():
          return []
        while True:
          if solved:
            break
          for r in self.iddfs_recurse(depth, []):
            solved = True
            yield r[0]
          depth += 1

    def tile_hueristic(self):
      h = 0
      for row in range(self.m):
        for col in range(self.n):
          if self.board[row][col] != 0:
            x = (self.board[row][col] - 1) / self.n
            y = (self.board[row][col] - 1) % self.n
            h += abs(x - row) + abs(y - col)
      return h

    # Required
    def find_solution_a_star(self):
        g = 0
        h = self.tile_hueristic()
        if self.is_solved():
          return []
        frontier = PriorityQueue()
        frontier.put((h, g, self, []))
        visited = set()
        while not frontier.empty():
          _, _, node, moves = frontier.get()
          if node.is_solved():
            return moves
          board_tuple = tuple(map(tuple, node.board))
          if board_tuple not in visited:
            visited.add(board_tuple)
            for successor in node.successors():
              g += 1
              move = successor[0]
              new_puzzle = successor[1]
              board_tuple = tuple(map(tuple, new_puzzle.board))
              if board_tuple not in visited:
                h = new_puzzle.tile_hueristic()
                new_cost = h + g
                frontier.put((new_cost, g, new_puzzle, moves + [move]))
############################################################
# Section 2: Grid Navigation
############################################################

def grid_move_valid(row, col, scene, move):
  if move == "up":
    if row > 0:
      new_row = row - 1
      if not scene[new_row][col]:
        return (new_row, col)
  elif move == "down":
    if row < (len(scene) - 1):
      new_row = row + 1
      if not scene[new_row][col]:
        return (new_row, col)
  elif move == "left":
    if col > 0:
      new_col = col - 1 
      if not scene[row][new_col]:
        return (row, new_col)
  elif move == "right":
    if col < (len(scene[0]) - 1):
      new_col = col + 1
      if not scene[row][new_col]:
        return (row, new_col)
  elif move == "up-left":
    if row > 0 and col > 0:
      new_row = row - 1
      new_col = col - 1
      if not scene[new_row][new_col]:
        return (new_row, new_col)
  elif move == "up-right":
    if row > 0 and col < (len(scene[0]) - 1):
      new_row = row - 1
      new_col = col + 1
      if not scene[new_row][new_col]:
        return (new_row, new_col)
  elif move == "down-left":
    if row < (len(scene) - 1) and col > 0:
      new_row = row + 1
      new_col = col - 1
      if not scene[new_row][new_col]:
        return (new_row, new_col)
  elif move == "down-right":
    if row < (len(scene) - 1) and col < (len(scene[0]) - 1):
      new_row = row + 1
      new_col = col + 1
      if not scene[new_row][new_col]:
        return (new_row, new_col)
  return ()

def grid_successors(curr, scene):
  curr_row = curr[0]
  curr_col = curr[1]
  allowed_moves = ['up', 'down', 'left', 'right', 'up-left', 'up-right', 'down-left', 'down-right']
  for move in allowed_moves:
    next = grid_move_valid(curr_row, curr_col, scene, move)
    if next:
      yield next

def is_diag(curr, next):
  if curr[0] == next[0] or curr[1] == next[1]:
    return False
  return True

def grid_heuristic(curr, goal):
  curr_row = curr[0]
  curr_col = curr[1]
  goal_row = goal[0]
  goal_col = goal[1]
  return (((curr_row - goal_row)**2 + (curr_col - goal_col)**2)**0.5)

def find_path(start, goal, scene):
    h = grid_heuristic(start, goal)
    if (scene[start[0]][start[1]]):
      return None
    if start == goal:
      return [start, goal]
    frontier = PriorityQueue()
    frontier.put((h, 0, 0, start, []))
    visited = set()
    while not frontier.empty():
      _, g, g_added, pos, moves = frontier.get()
      if pos == goal:
        moves = moves + [goal]
        return moves
      if pos not in visited:
        g += g_added
        moves = moves + [pos]
        visited.add(pos)
        for succ in grid_successors(pos, scene): 
            if succ not in visited:
              h = grid_heuristic(succ, goal)
              if is_diag(pos, succ): g_added = 2**0.5
              else: g_added = 1
              new_cost = h + g + g_added
              frontier.put((new_cost, g, g_added, succ, moves))

############################################################
# Section 3: Linear Disk Movement, Revisited
############################################################
def init_board_disks(length, n):
  front = [x + 1 for x in range(n)]
  end = [0] * (length - n)
  return front + end

def disk_successors(board):
  for index, disk in enumerate(board):
    if disk:
      if index + 1 < len(board) and not board[index + 1]:
        new_board = board.copy()
        forward_val = board[index + 1]
        new_board[index + 1] = disk
        new_board[index] = forward_val
        yield (index, index + 1), new_board
      if index + 1 < len(board) and board[index + 1] and index + 2 < len(board) and not board[index + 2]:
        new_board = board.copy()
        forward_val = board[index + 2]
        new_board[index + 2] = new_board[index]
        new_board[index] = forward_val
        yield (index, index + 2), new_board
      if index > 0 and not board[index - 1]:
        new_board = board.copy()
        backward_val = board[index - 1]
        new_board[index - 1] = disk
        new_board[index] = backward_val
        yield (index, index - 1), new_board
      if index - 1 > 0 and board[index - 1] and not board[index - 2]:
        new_board = board.copy()
        backward_val = board[index - 2]
        new_board[index - 2] = disk
        new_board[index] = backward_val
        yield (index, index - 2), new_board

def is_solved_distinct(board, l, n):
  output_board = [0] * (l - n) + [n - x for x in range(n)]
  return board == output_board

def disk_heuristic(board, n):
  h = 0
  l = len(board)
  for index, disk in enumerate(board):
    if disk:
      correct_pos = l - disk
      h += abs(correct_pos - index)
  return h

def solve_distinct_disks(length, n): 
    board = init_board_disks(length, n)
    g = 0
    h = disk_heuristic(board, n)
    if is_solved_distinct(board, length, n):
      return []
    frontier = PriorityQueue()
    frontier.put((h, g, board, [], ()))
    visited = set()
    while not frontier.empty():
      _, _, board, moves, move = frontier.get()
      board_tuple = tuple(board)
      if board_tuple not in visited:
        visited.add(board_tuple)
        if is_solved_distinct(board, length, n):
          return moves[1:] + [move]
        g += 1
        moves = moves + [move]
        for succ in disk_successors(board):
            if tuple(succ[1]) not in visited: 
              move = succ[0]
              new_board = succ[1]
              h = disk_heuristic(new_board, n)
              new_cost = h + g
              frontier.put((new_cost, g, new_board, moves, move))

############################################################
# Section 4: Feedback
############################################################

# Just an approximation is fine.
feedback_question_1 = 8

feedback_question_2 = """
I found the timing out challenging. I also found the grid distance challenging, 
as I went to office hours with the gradescope error and the TA could not find what was wrong. 
"""

feedback_question_3 = """
I like that we got to improve upon the same problem we worked on last assignment (with the disks)
"""
