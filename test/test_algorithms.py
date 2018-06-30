import unittest

from algorithms import \
    find_sum_combinations, \
    permutations


class TestAlgorithms(unittest.TestCase):
    def test_find_sum_combinations(self):
        """
        Checks we correctly find all possible combinations of numbers that
        sum to the provided total
        """
        self.assertEqual(find_sum_combinations(1, 2), [[0, 1],
                                                       [1, 0]])

        self.assertEqual(find_sum_combinations(1, 3), [[0, 0, 1],
                                                       [0, 1, 0],
                                                       [1, 0, 0]])

        self.assertEqual(find_sum_combinations(1, 4), [[0, 0, 0, 1],
                                                       [0, 0, 1, 0],
                                                       [0, 1, 0, 0],
                                                       [1, 0, 0, 0]])

        self.assertEqual(find_sum_combinations(2, 2), [[0, 2],
                                                       [1, 1],
                                                       [2, 0]])

        self.assertEqual(find_sum_combinations(2, 3), [[0, 0, 2],
                                                       [0, 1, 1],
                                                       [0, 2, 0],
                                                       [1, 0, 1],
                                                       [1, 1, 0],
                                                       [2, 0, 0]])

        self.assertEqual(find_sum_combinations(2, 4), [[0, 0, 0, 2],
                                                       [0, 0, 1, 1],
                                                       [0, 0, 2, 0],
                                                       [0, 1, 0, 1],
                                                       [0, 1, 1, 0],
                                                       [0, 2, 0, 0],
                                                       [1, 0, 0, 1],
                                                       [1, 0, 1, 0],
                                                       [1, 1, 0, 0],
                                                       [2, 0, 0, 0]])

        self.assertEqual(find_sum_combinations(3, 2), [[0, 3],
                                                       [1, 2],
                                                       [2, 1],
                                                       [3, 0]])

        self.assertEqual(find_sum_combinations(3, 3), [[0, 0, 3],
                                                       [0, 1, 2],
                                                       [0, 2, 1],
                                                       [0, 3, 0],
                                                       [1, 0, 2],
                                                       [1, 1, 1],
                                                       [1, 2, 0],
                                                       [2, 0, 1],
                                                       [2, 1, 0],
                                                       [3, 0, 0]])

        self.assertEqual(find_sum_combinations(3, 4), [[0, 0, 0, 3],
                                                       [0, 0, 1, 2],
                                                       [0, 0, 2, 1],
                                                       [0, 0, 3, 0],
                                                       [0, 1, 0, 2],
                                                       [0, 1, 1, 1],
                                                       [0, 1, 2, 0],
                                                       [0, 2, 0, 1],
                                                       [0, 2, 1, 0],
                                                       [0, 3, 0, 0],
                                                       [1, 0, 0, 2],
                                                       [1, 0, 1, 1],
                                                       [1, 0, 2, 0],
                                                       [1, 1, 0, 1],
                                                       [1, 1, 1, 0],
                                                       [1, 2, 0, 0],
                                                       [2, 0, 0, 1],
                                                       [2, 0, 1, 0],
                                                       [2, 1, 0, 0],
                                                       [3, 0, 0, 0]])

    def test_permutations(self):
        """
        Checks we correctly create a collection of all possible permutations
        for a possible input
        """
        values = [1, 2]
        expected = [(1, 2), (2, 1)]

        actual = [p for p in permutations(values)]
        self.assertListEqual(expected, actual)

        values = [1, 2, 3]
        expected = [(1, 2, 3), (1, 3, 2),
                    (2, 1, 3), (2, 3, 1),
                    (3, 1, 2), (3, 2, 1)]

        actual = [p for p in permutations(values)]
        self.assertListEqual(expected, actual)

        values = [1, 2, 3, 4]
        expected = [(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 3, 4, 2), (1, 4, 2, 3), (1, 4, 3, 2),
                    (2, 1, 3, 4), (2, 1, 4, 3), (2, 3, 1, 4), (2, 3, 4, 1), (2, 4, 1, 3), (2, 4, 3, 1),
                    (3, 1, 2, 4), (3, 1, 4, 2), (3, 2, 1, 4), (3, 2, 4, 1), (3, 4, 1, 2), (3, 4, 2, 1),
                    (4, 1, 2, 3,), (4, 1, 3, 2), (4, 2, 1, 3), (4, 2, 3, 1), (4, 3, 1, 2), (4, 3, 2, 1)]

        actual = [p for p in permutations(values)]
        self.assertListEqual(expected, actual)
