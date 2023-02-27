from unittest import TestCase
from unittest.mock import patch

from project import Project


class TestProject(TestCase):

    def test_has_zero_iterations(self):
        self.assertEqual([], Project(0, []).iterations)

    def test_has_zero_items(self):
        self.assertEqual([], Project(0, [1, 1, 2]).iterations)

    def test_given_ones(self):
        self.assertEqual([1], Project(1, [1]).iterations)

    def test_given_more_samples(self):
        self.assertEqual([1], Project(1, [1, 1, 1]).iterations)

    def test_given_different_samples(self):
        self.assertEqual([3], Project(1, [1, 2, 3]).iterations)

    def test_given_more_items(self):
        self.assertEqual([3, 3, 3, 3], Project(10, [1, 2, 3]).iterations)

    def test_uses_random_choice(self):
        with patch('random.choice', lambda s: s[len(s) - 2]):
            self.assertEqual([2] * 50, Project(100, [1, 2, 3]).iterations)

    def setUp(self):
        self.patched = patch('random.choice', lambda s: s[len(s) - 1])
        self.patched.start()

    def tearDown(self):
        self.patched.stop()
