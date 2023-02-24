from unittest import TestCase
from unittest.mock import Mock, patch

from project import Project


class TestProject(TestCase):

    def test_given_no_items_has_no_iterations(self):
        self.assertEqual([], Project(0, [1, 2, 3]).iterations)

    def test_given_no_samples_has_no_iterations(self):
        self.assertEqual([], Project(100, []).iterations)

    def test_runs_100_items_with_1s(self):
        self.assertEqual([1] * 100, Project(100, [1]).iterations)

    def test_runs_100_items_with_5s(self):
        with self.mock_random_choice() as mock_choice:
            self.assertEqual([5] * round(100 / 5), Project(100, [5]).iterations)
            mock_choice.assert_called()

    def test_runs_300_items_with_5s(self):
        with self.mock_random_choice() as mock_choice:
            self.assertEqual([5] * round(300 / 5), Project(300, [5]).iterations)
            mock_choice.assert_called()

    def test_runs_300_items_with_samples(self):
        with self.mock_random_choice() as mock_choice:
            self.assertEqual(100, len(Project(300, [1, 2, 3]).iterations))
            mock_choice.assert_called()

    @staticmethod
    def mock_random_choice():
        return patch('random.choice',
                     Mock(name='random.choice',
                          side_effect=lambda s: s[len(s) - 1]))
