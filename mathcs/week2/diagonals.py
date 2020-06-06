# Mathematical Thinking in Computer Science
# Week 2
#
# 16 diagonals.

import enum
import sys

from typing import List, Tuple


TOTAL_LINES = 16
SIZE = 5


class Square(enum.Enum):
  EMPTY = 0
  UP = 1
  DOWN = 2


def is_valid(p_pos: Tuple[int, int], p_val: Square,
             new: Tuple[int, int], val: Square) -> bool:
  # print(p_pos, p_val, new, val)
  if p_val == Square.EMPTY or val == Square.EMPTY:
    return True

  if p_pos[0] == new[0] or p_pos[1] == new[1]:
    return p_val == val

  if p_pos[1] == new[1] - 1:
    return p_val == Square.UP or p_val != val

  return p_val == Square.DOWN or p_val != val


def print_grid(grid: List[List[Square]]) -> None:
  for row in grid:
    for x in row:
      sys.stdout.write(('.', '/', '\\')[x.value])
    sys.stdout.write('\n')


def solve(grid: List[List[Square]], row: int, col: int, lines: int) -> None:
  # print(row, col, lines)
  if lines == TOTAL_LINES:
    print_grid(grid)
    sys.stdout.write('\n')
    sys.stdin.readline()
    return

  if row == len(grid):
    return

  for x in reversed(Square):

    valid = True
    for r, c in [(-1, -1), (-1, 0), (-1, 1), (0, -1)]:
      if not ((row + r < 0 or col + c < 0 or col + c >= len(grid[0])) or \
          (0 <= row + r and 0 <= col + c < len(grid[0]) and \
          is_valid((row + r, col + c), grid[row+r][col+c], (row, col), x))):
        valid = False
        break
    if not valid:
      continue

    grid[row][col] = x
    solve(grid,
        row if col + 1 < len(grid[0]) else row + 1,
        col + 1 if col + 1 < len(grid[0]) else 0,
        lines + 1 if x != Square.EMPTY else lines)
    grid[row][col] = Square.EMPTY


def main(argv):
  grid = [ [Square.EMPTY] * SIZE for _ in range(SIZE) ]
  solve(grid, 0, 0, 0)


if __name__ == '__main__':
  main(sys.argv)
