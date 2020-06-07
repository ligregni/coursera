#!/usr/bin/python3

# Design and Analysis of Algorithms
# Divide and Conquer, Sorting and Searching, and Randomized Algorithms

# Week 1
# Karatsuba's Multiplication

from typing import Tuple

import itertools

def _d(s: str) -> int:
  """
  Converts the digit character to its int form.
  """
  return ord(s) - ord('0')


def add(A: str, B: str) -> str:
  result = ''

  carry = 0
  for a, b in itertools.zip_longest(A[::-1], B[::-1]):
    x = _d(a) if a else 0
    x += _d(b) if b else 0
    x += carry
    result += chr((x % 10) + ord('0'))
    carry = x // 10

  result += '1' if carry else ''

  return result[::-1]


def _rlz(s: str) -> str:
  """
  Removes the leading zeroes from a number in string form.
  """
  x = 0
  while s[x] == '0' and x < len(s) - 1:
    x += 1
  return s[x:]


def subtract(A: str, B: str) -> str:
  result = ''

  borrow = 0
  for a, b in itertools.zip_longest(A[::-1], B[::-1]):
    m = _d(a)
    s = _d(b) if b else 0
    s += borrow
    if s > m:
      borrow = 1
      m += 10
    result += chr(m - s + ord('0'))

  return _rlz(result[::-1])


def get_halves(s: str, h: int) -> Tuple[str, str]:
  a = s[:(len(s)-h)] if len(s) > h else '0'
  b = s[(len(s)-h):] if len(s) > h else s
  return (a, b)


def _10n(s: str, p: int) -> str:
  """
  Multiplies the passed in number by 10^p.
  """
  return s + '0' * p


def multiply(X: str, Y: str) -> str:
  if not X or not Y:
    return '0'

  if len(X) == 1 and len(Y) == 1:
    return str(_d(X) * _d(Y))

  n = max(len(X), len(Y))
  h = n // 2

  a, b = get_halves(X, h)
  c, d = get_halves(Y, h)

  ac = multiply(a, c)
  bd = multiply(b, d)
  adcb = subtract(multiply(add(a, b), add(c, d)), add(ac, bd))

  return _rlz(add(add(_10n(ac, h * 2), _10n(adcb, h)), bd))
