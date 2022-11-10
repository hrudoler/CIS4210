############################################################
# CIS 521: adversarial_search
############################################################

student_name = "Helen Rudoler"

############################################################
# Imports
############################################################

# Include your imports here, if any are used.

import collections
import copy
import itertools
import random
import math

############################################################
# Section 1: Dominoes Game
############################################################

def create_dominoes_game(rows, cols):
    board = []
    for _ in range(rows):
      inner = []
      for _ in range(cols):
        inner.append(False)
      board.append(inner)
    return DominoesGame(board)

class DominoesGame(object):

    # Required
    def __init__(self, board):
        self.board = board
        self.num_rows = len(board)
        self.num_cols = len(board[0])

    def get_board(self):
        return self.board

    def reset(self):
        for row in range(self.num_rows):
          for col in range(self.num_cols):
            self.board[row][col] = False

    def is_legal_move(self, row, col, vertical):
        if self.board[row][col]:
          return False
        if row < 0 or col < 0 or row >= self.num_rows or col >= self.num_cols:
          return False
        if vertical:
          if row + 1 >= self.num_rows or self.board[row + 1][col]:
            return False
        elif col + 1 >= self.num_cols or self.board[row][col + 1]:
          return False
        return True

    def legal_moves(self, vertical):
        moves = []
        for row in range(self.num_rows):
          for col in range(self.num_cols):
            if self.is_legal_move(row, col, vertical):
              moves.append((row, col))
        return moves

    def perform_move(self, row, col, vertical):
        self.board[row][col] = True
        if vertical: self.board[row+1][col] = True
        else: self.board[row][col+1] = True

    def game_over(self, vertical):
        return not self.legal_moves(vertical)

    def copy(self):
        copy = [row[:] for row in self.board]
        return DominoesGame(copy)

    def successors(self, vertical):
        for move in self.legal_moves(vertical):
          successor = self.copy()
          successor.perform_move(move[0], move[1], vertical)
          yield (move, successor)

    def get_random_move(self, vertical):
        return random.choice(self.legal_moves(vertical))

    def evaluate(self, vertical, max):
      if max: vertical = not vertical
      max_moves = len(self.legal_moves(not vertical))
      min_moves = len(self.legal_moves(vertical))
      return max_moves - min_moves

    def ab_max(self, vertical, alpha, beta, limit):
      limit -= 1
      if self.game_over(vertical) or limit < 0: 
        return None, self.evaluate(vertical, True), 1
      best_move = None
      total_leaves = 0
      v = float('-inf')
      for move, new_game in self.successors(vertical):
        new_move, new_value, new_leaves = new_game.ab_min(not vertical, alpha, beta, limit)
        total_leaves += new_leaves
        if new_value > v:
          v = new_value
          best_move = move
          alpha = max(alpha, v)
        if v >= beta:
          break
      return best_move, v, total_leaves
    
    def ab_min(self,vertical, alpha, beta, limit):
      limit -= 1
      if self.game_over(vertical) or limit < 0: 
        return None, self.evaluate(vertical, False), 1
      best_move = None
      v = float('inf')
      total_leaves = 0
      for move, new_game in self.successors(vertical):
        new_move, new_value, new_leaves = new_game.ab_max(not vertical, alpha, beta, limit)
        total_leaves += new_leaves
        if new_value < v:
          v = new_value
          best_move = move
          beta = min(beta, v)
        if v <= alpha:
          break
      return best_move, v, total_leaves

    # Required
    def get_best_move(self, vertical, limit):
        best_move, best_value, total_leaves = self.ab_max(vertical, float('-inf'), float('inf'), limit)
        return best_move, best_value, total_leaves
############################################################
# Section 2: Feedback
############################################################

feedback_question_1 = 5

feedback_question_2 = """
I thought the alpha beta pruning was confusing at first, as in when to update those variables and to what. 
"""

feedback_question_3 = """
Wouldn't have changed it, thought it was fun
"""
