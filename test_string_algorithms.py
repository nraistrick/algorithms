import unittest

from string_algorithms import \
    all_unique_characters, \
    all_unique_characters_with_loop, \
    compress, \
    find_rotation_offset, \
    find_unique_substrings, \
    has_palindromic_permutation, \
    are_similar, \
    is_permutation, \
    is_permutation_with_inner_loop, \
    is_rotation, \
    rotate_clockwise, \
    rotate_clockwise_in_place, \
    url_encode, \
    url_encode_pythonic, \
    zero_matrix


class TestStringAlgorithms(unittest.TestCase):
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

    def test_compress(self):
        """
        Check the basic string compression works correctly
        """
        self.assertEqual("a2b3c4", compress("aabbbcccc"))
        self.assertEqual("a4b1c4d1", compress("aaaabccccd"))
        self.assertEqual("A2a2B3b3", compress("AAaaBBBbbb"))

        # If the compression doesn't result in a shorter string, then we
        # expect the original string to be returned
        self.assertEqual("abcd", compress("abcd"))
        self.assertEqual("aabbccdd", compress("aabbccdd"))

    def test_rotate(self):
        """
        Checks image rotation works correctly
        """
        # For square images
        self.assertEqual([[0, 1], [1, 0]], rotate_clockwise([[1, 0], [0, 1]]))
        self.assertEqual([[0, 1, 1], [1, 0, 1], [0, 1, 1]], rotate_clockwise([[0, 1, 0], [1, 0, 1], [1, 1, 1]]))

        # For non-square images
        self.assertEqual([[1, 0, 1], [0, 0, 1]], rotate_clockwise([[0, 1], [0, 0], [1, 1]]))
        self.assertEqual([[1, 1], [0, 0], [1, 0]], rotate_clockwise([[1, 0, 1], [0, 0, 1]]))

    def test_rotate_in_place(self):
        """
        Checks in-place image rotation works correctly
        """
        self.assertEqual([[0, 1], [1, 0]],
                         rotate_clockwise_in_place([[1, 0], [0, 1]]))

        self.assertEqual([[0, 1, 1], [1, 0, 1], [0, 1, 1]],
                         rotate_clockwise_in_place([[0, 1, 0], [1, 0, 1], [1, 1, 1]]))

        self.assertEqual([[0, 0, 1, 1], [1, 1, 1, 1], [1, 0, 0, 1], [0, 1, 0, 1]],
                         rotate_clockwise_in_place([[0, 1, 1, 0], [1, 0, 1, 0], [0, 0, 1, 1], [1, 1, 1, 1]]))

    def test_zero_matrix(self):
        """
        Checks that corresponding rows and columns are correctly zeroed for
        any identified zero elements
        """
        self.assertEqual([[1, 1, 0], [0, 0, 0], [1, 1, 0]],
                         zero_matrix([[1, 1, 1], [1, 1, 0], [1, 1, 1]]))

        self.assertEqual([[0, 1, 1, 0], [0, 0, 0, 0], [0, 1, 1, 0], [0, 0, 0, 0]],
                         zero_matrix([[1, 1, 1, 1], [1, 1, 1, 0], [1, 1, 1, 1], [0, 1, 1, 1]]))

    def test_find_unique_substrings(self):
        """
        Checks that all unique substrings are found for the provided pair
        of strings
        """
        self.assertEqual(["h", "e", "o", "he", "ll", "lo", "llo"],
                         [i for i in find_unique_substrings("hello", "llohe")])

        self.assertEqual(["b", "ab"],
                         [i for i in find_unique_substrings("aab", "aba")])

        self.assertEqual(["d", "aaa", "bbb"],
                         [i for i in find_unique_substrings("aaabbbcd", "bbbdaaa")])

        self.assertEqual([],
                         [i for i in find_unique_substrings("aaaaa", "aaaaa")])

    def test_find_rotation_offset(self):
        """
        Checks the rotation offset between two strings is calculated correctly
        """
        self.assertEqual(0, find_rotation_offset("ab", "ab"))
        self.assertEqual(0, find_rotation_offset("aaaaa", "aaaaa"))
        self.assertEqual(1, find_rotation_offset("ab", "ba"))
        self.assertEqual(2, find_rotation_offset("hello", "lohel"))
        self.assertEqual(3, find_rotation_offset("abcde", "cdeab"))
        self.assertEqual(4, find_rotation_offset("abcde", "bcdea"))

        self.assertRaises(Exception, find_rotation_offset, "abc", "aaa")

    def test_is_rotation(self):
        """
        Checks if two strings are identical except that they have had some
        of their characters rotated
        """
        self.assertTrue(is_rotation("abc", "bca"))
        self.assertTrue(is_rotation("abcde", "cdeab"))
        self.assertTrue(is_rotation("helloworld", "worldhello"))

        self.assertFalse(is_rotation("abc", "bac"))
        self.assertFalse(is_rotation("abcde", "acbde"))
        self.assertFalse(is_rotation("helloworld", "worlhdello"))

        self.assertRaises(ValueError, is_rotation, "helloworld", "worldello")


if __name__ == '__main__':
    unittest.main()
