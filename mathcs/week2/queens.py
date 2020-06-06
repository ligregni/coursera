# Mathematical Thinking in Computer Science
# Week 2
#
# Number of solutions for the 8 Queens puzzle.

import sys

from typing import List, Tuple


QUEENS = 8


def is_valid(board: List[int]):
  for i in range(len(board) - 1):
    if len(board) - 1 - i == abs(board[-1] - board[i]):
      return False

  return True


def print_board(board: List[int]) -> None:
  for i, j in enumerate(board):
    for k in range(len(board)):
      sys.stdout.write('Q' if k == j else '.')
    sys.stdout.write('\n')
  print()

def solve(board: List[int], n: int, count: List[int]) -> None:
  if len(board) == n:
    print_board(board)
    count[0] += 1
    return

  for i in range(n):
    if i not in board:
      board.append(i)
      if is_valid(board):
        solve(board, n, count)
      board.pop()


def main(argv):
  count = [0]
  solve(list(), QUEENS, count)
  print(count[0])


if __name__ == '__main__':
  main(sys.argv)
