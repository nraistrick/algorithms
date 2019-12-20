import unittest

from sorting_and_searching_algorithms import merge_two_sorted_lists


class TestSortingAndSearchingAlgorithms(unittest.TestCase):
    def test_merge_two_sorted_lists(self):
        """
        Checks we can merge one list into another
        """
        a = [0, 2, 3, None, None, None, None]
        b = [0, 1, 2, 4]
        expected = [0, 0, 1, 2, 2, 3, 4]

        result = merge_two_sorted_lists(a, b)
        self.assertListEqual(expected, result)
