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


class SubtractionTest(unittest.TestCase):

  def test_zero_when_two_zeroes(self):
    self.assertEqual(karatsuba.subtract('0', '0'), '0')

  def test_zero_when_equal(self):
    self.assertEqual(karatsuba.subtract('1234', '1234'), '0')

  def test_minuendo_when_substraendo_is_zero(self):
    self.assertEqual(karatsuba.subtract('1234', '0'), '1234')

  def test_subtraction_minus_one(self):
    self.assertEqual(karatsuba.subtract('1234', '1'), '1233')

  def test_subtraction_minus_all_but_one(self):
    self.assertEqual(karatsuba.subtract('1234', '1233'), '1')

  def test_subtraction_no_borrow(self):
    self.assertEqual(karatsuba.subtract('9876', '4321'), '5555')

  def test_subtraction_borrow_follows(self):
    self.assertEqual(karatsuba.subtract('10000', '1'), '9999')

  def test_subtraction_borrow(self):
    self.assertEqual(karatsuba.subtract('10000', '1234'), '8766')


class GetHalvesTest(unittest.TestCase):

  def test_halves_large_number_even_digits(self):
    self.assertEqual(karatsuba.get_halves('12345678', 4), ('1234', '5678'))

  def test_halves_large_number_odd_digits(self):
    self.assertEqual(karatsuba.get_halves('1234567', 4), ('123', '4567'))

  def test_halves_small_number_one_and_one(self):
    self.assertEqual(karatsuba.get_halves('12', 1), ('1', '2'))

  def test_halves_small_number_large_n(self):
    self.assertEqual(karatsuba.get_halves('12', 2), ('0', '12'))

  def test_halves_small_number_largest_n(self):
    self.assertEqual(karatsuba.get_halves('12', 3), ('0', '12'))


class MultiplicationTest(unittest.TestCase):

  def test_multiply_by_zero_a(self):
    self.assertEqual(karatsuba.multiply('1234', '0'), '0')

  def test_multiply_by_zero_b(self):
    self.assertEqual(karatsuba.multiply('0', '1234'), '0')

  def test_multiply_by_one_a(self):
    self.assertEqual(karatsuba.multiply('1234', '1'), '1234')

  def test_multiply_by_one_b(self):
    self.assertEqual(karatsuba.multiply('1', '1234'), '1234')

  def test_multiply_one_digit(self):
    self.assertEqual(karatsuba.multiply('2', '7'), '14')

  def test_multiply_many_digits(self):
    self.assertEqual(karatsuba.multiply('46', '134'), '6164')

  def test_multiply_many_digits_two(self):
    self.assertEqual(karatsuba.multiply('100', '46'), '4600')

  def test_multiply_many_digits_long(self):
    self.assertEqual(karatsuba.multiply('1234', '5678'), '7006652')

