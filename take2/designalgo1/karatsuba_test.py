#!/usr/bin/python3

import unittest

import karatsuba

class AdditionTest(unittest.TestCase):

  def test_zero_when_two_zeroes(self):
    self.assertEqual(karatsuba.add('0', '0'), '0')

  def test_single_digit_a_when_b_is_zero(self):
    self.assertEqual(karatsuba.add('9', '0'), '9')

  def test_single_digit_b_when_a_is_zero(self):
    self.assertEqual(karatsuba.add('0', '9'), '9')

  def test_a_when_b_is_zero(self):
    self.assertEqual(karatsuba.add('9876200', '0'), '9876200')

  def test_b_when_a_is_zero(self):
    self.assertEqual(karatsuba.add('0', '9876200'), '9876200')

  def test_a_plus_b_no_carry_needed(self):
    self.assertEqual(karatsuba.add('1111', '2222'), '3333')

  def test_a_plus_b_carry_needed(self):
    self.assertEqual(karatsuba.add('1', '9999'), '10000')

  def test_a_plus_b_large_b_larger_a(self):
    self.assertEqual(karatsuba.add('123456', '9999'), '133455')

  def test_a_plus_b_large_a_larger_b(self):
    self.assertEqual(karatsuba.add('9999', '123456'), '133455')

