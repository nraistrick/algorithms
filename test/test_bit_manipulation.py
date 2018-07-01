import unittest

from bit_manipulation_algorithms import \
    insert_bits


class TestBitManipulationAlgorithms(unittest.TestCase):
    def test_insert_bits(self):
        """
        Checks we correctly insert the bits from a number into a
        specific place in another number
        """
        n = int("10000000000", 2)
        m = int("10011", 2)
        i = 2
        j = 6

        expected = int("10001001100", 2)
        actual = insert_bits(n, m, i, j)

        self.assertEqual(bin(expected), bin(actual))
