from unittest import TestCase
from unittest.mock import patch

from monty import Monty


class TestMonty(TestCase):

    @patch('monty.Project.__init__', return_value=None)
    def test_runs_a_project_many_times(self, mocked_project):
        Monty(100, [1, 2, 3, 4], passes=100)
        mocked_project.assert_called_with(100, [1, 2, 3, 4])
        self.assertEqual(100, mocked_project.call_count)

    def test_forecasts_empty(self):
        self.expect_forecast(0, 0, [])

    def test_forecasts(self):
        self.expect_forecast(100, 100, [1])

    def test_forecasts_with_more_interesting_data(self):
        self.expect_forecast(34, 300, [1, 3, 5, 7, 9])

    def test_forecasts_with_more_certainty(self):
        self.expect_forecast(34, 300, [1, 3, 5, 7, 9], 95)

    def expect_forecast(self, expected, items, samples, probability=85):
        with patch('random.choice', lambda s: s[len(s) - 1]):
            with patch('numpy.percentile', side_effect=lambda s, p: s[p]) as mocked_percentile:
                self.assertEqual(expected, Monty(items, samples).forecast(probability))
                mocked_percentile.assert_called_with(any(), probability)

def any():
    class Any:
        def __eq__(self, other):
            return True

    return Any()