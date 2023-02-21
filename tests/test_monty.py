import unittest

from monty import Monty


class TestMonty(unittest.TestCase):

    def test_zero_items_returns_zero(self):
        self.assertEqual(
            [(75, 0), (85, 0), (95, 0)],
            self.forecast(0, [0, 0, 0]))  # add assertion here

    def test_zero_data_returns_zero(self):
        self.assertEqual(
            [(75, 0), (85, 0), (95, 0)],
            self.forecast(10, [0, 0, 0]))  # add assertion here

    def test_one_hundred_items(self):
        self.assertEqual(
            [(75, 16), (85, 25), (95, 32)],
            self.forecast(100, [10, 8, 9, 4, 1, 4, 4, 2, 10, 20, 6, 7, 8]))  # add assertion here

    def test_three_hundred_items(self):
        self.assertEqual(
            [(75, 7), (85, 9), (95, 14)],
            self.forecast(300, [0, 23, 56, 34, 54, 56, 76, 1]))  # add assertion here

    def setUp(self):
        self.mockChoiceCalls = 1

    def mock_choice(self, data):
        self.mockChoiceCalls += 1
        seed = self.mockChoiceCalls / max(1, sum(data))
        index = round(seed * 10) % len(data)
        return data[index]

    def forecast(self, items, data):
        return Monty(data,
                     passes=100,
                     choose=self.mock_choice)\
            .forecast(items)
