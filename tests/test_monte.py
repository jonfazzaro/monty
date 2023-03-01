from unittest import TestCase
from unittest.mock import patch

from monte import Monte


class TestMonte(TestCase):

    def test_simulates_a_project_with_no_items(self):
        self.assertEqual([], Monte(0, [1]).simulations)

    def test_simulates_a_project_with_no_samples(self):
        self.assertEqual([], Monte(10, []).simulations)

    def test_passes_default_to_10000(self):
        self.assertEqual(10000, Monte(0, []).PASSES)

    def test_simulates_a_project(self):
        subject = self.monte(100, [12, 24, 13, 45, 6, 7, 17])
        self.assertEqual([5, 6, 7], subject.simulations)
        self.assertEqual(7, subject.forecast())

    def test_simulates_another_project(self):
        subject = self.monte(100, [4, 5, 6, 34, 4, 5, 6, 3, 4, 5, 3, 4])
        self.assertEqual([16, 16, 17], subject.simulations)
        self.assertEqual(17, subject.forecast())
        self.assertEqual(16, subject.forecast(50))

    @staticmethod
    def monte(items, samples):
        with patch('random.choice', side_effect=samples * items):
            return Monte(items, samples, 3)
