import unittest

from algorithms import \
    all_unique_characters, \
    all_unique_characters_with_loop, \
    find_sum_combinations, \
    is_permutation, \
    is_permutation_with_inner_loop


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

    def test_all_unique_characters(self):
        """
        Checks we correctly identify strings with unique and non-unique
        combinations of characters
        """
        functions = all_unique_characters, all_unique_characters_with_loop

        for f in functions:
            self.assertTrue(f("abc"))
            self.assertTrue(f("gdfneo"))
            self.assertTrue(f("10x93pl2wd"))

            self.assertFalse(f("aaa"))
            self.assertFalse(f("aba"))
            self.assertFalse(f("aab"))
            self.assertFalse(f("abcdefdgh"))
            self.assertFalse(f("3420120a"))

    def test_is_permutation(self):
        """
        Checks we correctly identify strings that are permutations of each other
        """
        functions = is_permutation, is_permutation_with_inner_loop

        for f in functions:
            self.assertTrue(f("abc", "bac"))
            self.assertTrue(f("hello", "eollh"))
            self.assertTrue(f("123def", "f2ed31"))

            self.assertFalse(f("abc", "hello"))
            self.assertFalse(f("abc", "abcd"))
            self.assertFalse(f("123def", "123dff"))


if __name__ == '__main__':
    unittest.main()
