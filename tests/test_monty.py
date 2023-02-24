from unittest import TestCase

from monty import Monty


class TestMonty(TestCase):

    def test_returns_zero_given_no_items(self):
        self.assertEqual(
            0, Monty([1, 2, 3], 0).forecast())

    def test_returns_zero_given_items_and_no_samples(self):
        self.assertEqual(
            0, Monty([0], 100).forecast())

    def test_one_hundred_items(self):
        self.assertEqual(
            6, Monty([10, 20, 30], 100).forecast())

    def test_three_hundred_items(self):
        self.assertEqual(
            26, Monty([10, 20, 30, 6, 7, 8], 300).forecast())

    def test_three_hundred_items_highly_likely(self):
        self.assertEqual(
            28, Monty([10, 20, 30, 6, 7, 8], 300).forecast(95))
