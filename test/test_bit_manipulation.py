import unittest

from bit_manipulation_algorithms import \
    binary_to_string, \
    count_binary_ones, \
    count_bits_to_flip, \
    count_longest_one_sequence, \
    draw_line, \
    flip_a_zero_bit, \
    flip_bit_to_win, \
    get_bit, \
    get_next_number, \
    insert_bits, \
    pairwise_swap, \
    set_bit


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

    def test_flip_bit_to_win(self):
        """
        Checks we correctly find the longest possible sequence of ones by
        flipping a single bit in a sequence from a 0 to a 1
        """
        self.assertEqual(1, flip_bit_to_win('00000000'))
        self.assertEqual(3, flip_bit_to_win('01100100'))
        self.assertEqual(5, flip_bit_to_win('01110100'))
        self.assertEqual(8, flip_bit_to_win('11111111'))
        self.assertEqual(8, flip_bit_to_win('11011101111'))

    def test_count_longest_one_sequence(self):
        """
        Checks that we correctly count the longest sequence of ones in
        a provided string containing binary digits
        """
        self.assertEqual(1, count_longest_one_sequence("0100"))
        self.assertEqual(2, count_longest_one_sequence("0110"))
        self.assertEqual(3, count_longest_one_sequence("1110"))
        self.assertEqual(4, count_longest_one_sequence("1111"))

        self.assertEqual(1, count_longest_one_sequence("100000000"))
        self.assertEqual(1, count_longest_one_sequence("101010101"))
        self.assertEqual(3, count_longest_one_sequence("100110111"))
        self.assertEqual(4, count_longest_one_sequence("111101100"))

    def test_flip_a_zero_bit(self):
        """
        Tests we correctly flip any zero bits that have a neighbouring one bit
        with the ultimate aim of creating the longest sequence of ones possible
        """
        self.assertListEqual(["1100", "0110", "0101"], list(flip_a_zero_bit("0100")))
        self.assertListEqual(["1101", "0111"], list(flip_a_zero_bit("0101")))
        self.assertListEqual(["100101", "010101", "001101", "000111"], list(flip_a_zero_bit("000101")))
        self.assertListEqual(["110101", "011101", "010111"], list(flip_a_zero_bit("010101")))

    def test_get_next_number(self):
        """
        Checks we correctly get the next positive number in a sequence that
        has the same number of binary 1s as the provided number
        """
        self.assertEqual(2, get_next_number(1))
        self.assertEqual(4, get_next_number(2))
        self.assertEqual(5, get_next_number(3))
        self.assertEqual(8, get_next_number(4))
        self.assertEqual(6, get_next_number(5))

        self.assertRaises(ValueError, get_next_number, -1)
        self.assertRaises(ValueError, get_next_number, -100)

    def test_get_binary_ones(self):
        """
        Checks we correctly count the number of binary ones in a sequence
        """
        self.assertEqual(1, count_binary_ones(1))
        self.assertEqual(1, count_binary_ones(2))
        self.assertEqual(2, count_binary_ones(3))
        self.assertEqual(1, count_binary_ones(4))
        self.assertEqual(2, count_binary_ones(5))

        self.assertEqual(2, count_binary_ones(10))
        self.assertEqual(4, count_binary_ones(15))
        self.assertEqual(5, count_binary_ones(31))

    def test_count_bits_to_flip(self):
        """
        Checks we correctly count the number of bits to flip to convert one
        number to another number
        """
        self.assertEqual(2, count_bits_to_flip(0b111, 0b001))
        self.assertEqual(3, count_bits_to_flip(0b111, 0b000))
        self.assertEqual(4, count_bits_to_flip(0b1111, 0b000))
        self.assertEqual(5, count_bits_to_flip(0b01010, 0b10101))
        self.assertEqual(6, count_bits_to_flip(0b01010111, 0b01101000))

    def test_pairwise_swap(self):
        """
        Checks we correctly switch the odd and even bits of a number
        """
        self.assertEqual(0b01, pairwise_swap(0b10))
        self.assertEqual(0b0101, pairwise_swap(0b1010))
        self.assertEqual(0b11110001, pairwise_swap(0b11110010))
        self.assertEqual(0b0101010101, pairwise_swap(0b1010101010))

        self.assertRaises(ValueError, pairwise_swap, 2 ** 32)

    def test_draw_line(self):
        """
        Checks we correctly draw a line of pixels on a byte array which
        makes up a screen. Each bit represents a single pixel.
        """
        self.assertEqual([0b00111000],
                         draw_line([0b00000000], 1, 2, 4, 0))

        self.assertEqual([0b00000111, 0b11111000],
                         draw_line([0b00000000] * 2, 2, 5, 12, 0))

        self.assertEqual([0b00000000, 0b00000000, 0b00011111, 0b11000000],
                         draw_line([0b00000000] * 4, 2, 3, 9, 1))

        self.assertEqual([0b00000000, 0b00000000, 0b00000000, 0b00000011, 0b11111111, 0b11000000],
                         draw_line([0b00000000] * 6, 3, 6, 17, 1))

        self.assertEqual([0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00011000, 0b00000000],
                         draw_line([0b00000000] * 6, 2, 4, 3, 2))

    def test_set_bit(self):
        """
        Checks we correctly set a bit in the provided byte
        """
        self.assertEqual(0b10000000, set_bit(0b00000000, 0))
        self.assertEqual(0b00100000, set_bit(0b00000000, 2))
        self.assertEqual(0b00000100, set_bit(0b00000000, 5))
        self.assertEqual(0b00000001, set_bit(0b00000000, 7))
        self.assertEqual(0b11100001, set_bit(0b11100000, 7))
        self.assertEqual(0b11100011, set_bit(0b11100001, 6))
