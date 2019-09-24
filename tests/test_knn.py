import unittest

from utils.knn import get_neighbors, get_classification


class KnnTestCase(unittest.TestCase):
    array = [5.1, 3.5, 1.4, 0.2, 1]
    neighbors = [(0.5, 1), (0.7, 2), (0.6, 1), (0.8, 2), (0.9, 3)]
    quantity = 3

    def test_get_neighbors(self):
        expect_res = [(0.5, 1), (0.6, 1), (0.7, 2)]
        res = get_neighbors(self.neighbors, self.quantity)
        self.assertEqual(res, expect_res)

    def test_get_classification(self):
        expect_classification = self.array[-1]

        classification = get_classification(self.neighbors, self.quantity)

        self.assertEqual(classification, expect_classification)

    def test_get_classification_error(self):
        classification = get_classification(self.neighbors, 4)

        self.assertFalse(classification)

