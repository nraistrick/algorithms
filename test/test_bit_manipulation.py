import unittest

from bit_manipulation_algorithms import \
    binary_to_string, \
    get_bit, \
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

    def test_binary_to_string(self):
        """
        Checks we correctly convert a floating point number
        to its binary representation
        """
        self.assertRaises(ValueError, binary_to_string, 2.5)
        self.assertRaises(ValueError, binary_to_string, -1.3)

        self.assertRaises(ValueError, binary_to_string, 0.0123456789012345678901234567890123456789)

        self.assertEqual("001100000010111000110000",
                         binary_to_string(0.0))

        self.assertEqual("001100000010111000110101",
                         binary_to_string(0.5))

        self.assertEqual("0011000000101110001100010011001000110101",
                         binary_to_string(0.125))

        self.assertEqual("00110000001011100011000000110110001100100011001000110101",
                         binary_to_string(0.06225))

    def test_get_bit(self):
        """
        Tests getting a single bit from a provided value
        """
        self.assertEqual(0, get_bit(0b1000, 0))
        self.assertEqual(0, get_bit(0b1000, 1))
        self.assertEqual(0, get_bit(0b1000, 2))
        self.assertEqual(1, get_bit(0b1000, 3))

        self.assertEqual(0, get_bit(0b1000, 4))
        self.assertEqual(0, get_bit(0b1000, 5))
        self.assertEqual(0, get_bit(0b1000, 6))
        self.assertEqual(0, get_bit(0b1000, 7))

        self.assertRaises(ValueError, get_bit, 0b1000, -1)
