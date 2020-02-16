import unittest

from sorting_and_searching_algorithms import merge_two_sorted_lists,\
    sort_by_anagram,\
    search_in_rotated_array


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

    def test_sort_by_anagram(self):
        """
        Checks we correctly sort and group a list by strings that are
        anagrams of each other
        """
        unsorted = ["a", "b"]
        expected = ["a", "b"]
        self.assertListEqual(sort_by_anagram(unsorted), expected)

        unsorted = ["c", "b", "a"]
        expected = ["c", "b", "a"]
        self.assertListEqual(sort_by_anagram(unsorted), expected)

        unsorted = ["ab", "c", "ba"]
        expected = ["ab", "ba", "c"]
        self.assertListEqual(sort_by_anagram(unsorted), expected)

        unsorted = ["cabde", "c", "ebadc"]
        expected = ["cabde", "ebadc", "c"]
        self.assertListEqual(sort_by_anagram(unsorted), expected)

        unsorted = ["xyz", "xyw", "yzx"]
        expected = ["xyz", "yzx", "xyw"]
        self.assertListEqual(sort_by_anagram(unsorted), expected)

        unsorted = ["xyz", "yyy", "xzx", "yxz", "jef", "xyz"]
        expected = ["xyz", "yxz", "xyz", "yyy", "jef", "xzx"]
        self.assertListEqual(sort_by_anagram(unsorted), expected)

        unsorted = ["xyz", "yyy", "xzx", "yxz", "yyy", "xyz", "yyy"]
        expected = ["xyz", "yxz", "xyz", "yyy", "yyy", "yyy", "xzx"]
        self.assertListEqual(sort_by_anagram(unsorted), expected)

    def test_search_in_rotated_array(self):
        array = [1, 2, 3, 4, 5, 6]
        search_value = 1
        expected_index = 0
        actual_index = search_in_rotated_array(array, search_value)
        self.assertEqual(expected_index, actual_index)

        array = [1, 2, 3, 4, 5, 6]
        search_value = 5
        expected_index = 4
        actual_index = search_in_rotated_array(array, search_value)
        self.assertEqual(expected_index, actual_index)

        rotated_array = [4, 5, 6, 1, 2, 3]
        search_value = 5
        expected_index = 1
        actual_index = search_in_rotated_array(rotated_array, search_value)
        self.assertEqual(expected_index, actual_index)

        rotated_array = [4, 5, 6, 1, 2, 3]
        search_value = 3
        expected_index = 5
        actual_index = search_in_rotated_array(rotated_array, search_value)
        self.assertEqual(expected_index, actual_index)

        rotated_array = [6, 1, 2, 3, 4, 5]
        search_value = 6
        expected_index = 0
        actual_index = search_in_rotated_array(rotated_array, search_value)
        self.assertEqual(expected_index, actual_index)
