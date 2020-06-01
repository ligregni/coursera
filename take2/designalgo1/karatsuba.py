#!/usr/bin/python3

# Design and Analysis of Algorithms
# Divide and Conquer, Sorting and Searching, and Randomized Algorithms

# Week 1
# Karatsuba's Multiplication

import itertools

def add(A: str, B: str) -> str:
  result = ''

  carry = 0
  for a, b in itertools.zip_longest(A[::-1], B[::-1]):
    x = ord(a) - ord('0') if a else 0
    x += ord(b) - ord('0') if b else 0
    x += carry
    result += chr((x % 10) + ord('0'))
    carry = x // 10

  result += '1' if carry else ''

  return result[::-1]


