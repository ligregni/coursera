#!/usr/bin/python3

import unittest

import karatsuba

class AdditionTest(unittest.TestCase):

  def test_zero_when_two_zeroes(self):
    self.assertEqual(karatsuba.add('0', '0'), '0')
