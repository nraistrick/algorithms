import unittest

from algorithms import \
    all_unique_characters, \
    all_unique_characters_with_loop, \
    find_sum_combinations, \
    has_palindromic_permutation, \
    are_similar, \
    is_permutation, \
    is_permutation_with_inner_loop, \
    url_encode, \
    url_encode_pythonic


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

    def test_url_encode(self):
        """
        Checks we correctly URL encode spaces using a non-pythonic
        algorithm implementation
        """
        self.assertEqual("Mr%20John%20Smith", url_encode("Mr John Smith    ", 13))
        self.assertEqual("Mr%20David%20Barrimore", url_encode("Mr David Barrimore    ", 18))

    def test_url_encode_pythonic(self):
        """
        Checks we correctly URL encode spaces using a pythonic
        algorithm implementation
        """
        self.assertEqual("Mr%20John%20Smith", url_encode_pythonic("Mr John Smith"))
        self.assertEqual("Mr%20David%20Barrimore", url_encode_pythonic("Mr David Barrimore"))

    def test_has_palindromic_permutation(self):
        """
        Checks we correctly identify strings with a permutation
        that is also a palindrome
        """
        self.assertTrue(has_palindromic_permutation("aba"))
        self.assertTrue(has_palindromic_permutation("tact coa"))
        self.assertTrue(has_palindromic_permutation("tact coa xyyx eedd"))

        self.assertFalse(has_palindromic_permutation("abc"))
        self.assertFalse(has_palindromic_permutation("dfg ada lob"))
        self.assertFalse(has_palindromic_permutation("123ad"))

    def test_is_similar(self):
        """
        Checks we correctly identify strings that are no more than one move
        away from being the same as another string
        """
        # Typical usage
        self.assertTrue(are_similar("pale", "ple"))
        self.assertTrue(are_similar("ple", "pale"))
        self.assertTrue(are_similar("pales", "pale"))
        self.assertTrue(are_similar("pale", "bale"))

        self.assertFalse(are_similar("no", "true"))
        self.assertFalse(are_similar("abcd", "abcdef"))
        self.assertFalse(are_similar("pale", "bake"))

        # Edge cases
        self.assertTrue(are_similar("", ""))
        self.assertTrue(are_similar("", "a"))
        self.assertTrue(are_similar("a", ""))


if __name__ == '__main__':
    unittest.main()
