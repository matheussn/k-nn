import unittest

from accuracy.accuracy import get_accuracy


class AccuracyTestCase(unittest.TestCase):
    def test_get_accuracy(self):
        expected_accuracy = 100

        value = get_accuracy(150, 150)

        self.assertEqual(value, expected_accuracy)
