from unittest import TestCase, mock
from monty import Monty


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

    def __forecast(self, items, data):
        self.call_count = 0

        def mock_choice(samples):
            self.call_count += 1
            index = round(self.call_count/10) % len(samples)
            return samples[index]

        with mock.patch('random.choice', mock_choice):
            return Monty(data).forecast(items)
