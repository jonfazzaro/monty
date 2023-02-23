from unittest import TestCase, mock
from monty import Monty
from tests.fakes import FakeRandom


class TestMonty(TestCase):

    def test_zero_items_returns_zero(self):
        self.assertEqual(
            [(75, 0), (85, 0), (95, 0)],
            self.__forecast(0, [0, 0, 0]))

    def test_zero_data_returns_zero(self):
        self.assertEqual(
            [(75, 0), (85, 0), (95, 0)],
            self.__forecast(10, [0, 0, 0]))

    def test_one_hundred_items(self):
        self.assertEqual(
            [(75, 16), (85, 25), (95, 32)],
            self.__forecast(100, [10, 8, 9, 4, 1, 4, 4, 2, 10, 20, 6, 7, 8]))

    def test_three_hundred_items(self):
        self.assertEqual(
            [(75, 7), (85, 9), (95, 31)],
            self.__forecast(300, [0, 23, 56, 34, 54, 56, 76, 1]))

    @staticmethod
    def __forecast(items, data):
        with mock.patch('random.choice', FakeRandom().choice):
            return Monty(data).forecast(items)
