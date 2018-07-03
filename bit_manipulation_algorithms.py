"""
Contains a selection of bit manipulation related algorithms
"""

from cStringIO import StringIO


def insert_bits(first, second, i, j):
    """
    Inserts bit from one number into another between a start
    and stop bit

    :param int first: The number to insert the bits into
    :param int second: The number containing the bits to insert into the other number
    :param int i: The LSB to finish inserting at
    :param int j: The MSB to start inserting at
    :return: The first value with the second value inserted at the given offset
    :rtype: int
    """
    second <<= i

    # Create a mask to clear the existing bits at the insertion location
    clear = 0
    bits_to_insert = j - i + 1
    for _ in range(bits_to_insert):
        clear <<= 1
        clear += 1

    clear = ~clear
    first &= clear

    # Insert the new bits into the first number
    first |= second

    return first


def binary_to_string(value):
    """
    Prints a floating point number between 0 and 1 in its binary form

    If the number cannot be represented accurately in 32 characters or less,
    an error will be printed instead

    :param float value: The value to print as binary. Must be between 0 and 1.
    """
    # The maximum number of floating point characters to display as binary
    max_characters = 32

    # Can ignore numbers smaller than this
    required_accuracy = 0.00001

    if value < 0 or value > 1:
        raise ValueError("Invalid input argument")

    characters = ['0', '.']
    while len(characters) < max_characters:
        value *= 10

        v = int(value)
        characters.append(str(v))
        value -= v

        if value < required_accuracy:
            break

    if value > required_accuracy:
        raise ValueError("Number cannot be represented accurately within %d digits" %
                         max_characters)

    bits = StringIO()
    for c in characters:
        for bit_number in range(7, -1, -1):
            bits.write(str(get_bit(ord(c), bit_number)))

    return bits.getvalue()


def get_bit(value, bit):
    """
    Get's a specific bit from the provided number

    :param int value: A number to get the bit of
    :param bit: The number of the bit
    :return: The bit value, 0 or 1
    :rtype: int
    """
    if bit < 0:
        raise ValueError("Bit number must be 0 or greater")

    return 1 if value & 1 << bit != 0 else 0


def flip_bit_to_win(binary_digits):
    """
    Finds the longest sequence of 1 digits that can be made by flipping
    a single bit in a sequence binary digits from a 0 to a 1

    :param str binary_digits: A sequence of binary 0s and 1s
    :return: The longest sequence of 1s that can be created by one bit flip
    :rtype: int
    """
    if '0' not in binary_digits:
        return len(binary_digits)

    longest_sequence = 0
    for sequence in flip_a_zero_bit(binary_digits):
        count = count_longest_one_sequence(sequence)
        if count > longest_sequence:
            longest_sequence = count

    return longest_sequence


def count_longest_one_sequence(binary):
    """
    Finds the length of the longest sequence of 1s in a binary sequence

    :param str binary: A sequence of binary 0s and 1s
    :return: The length of the longest sequence of 1s
    :rtype: int
    """
    longest_sequence = 0
    counting = True
    current = 0

    for b in binary:

        if b == '0' and counting:
            if current > longest_sequence:
                longest_sequence = current
            counting = False
            current = 0

        elif b == '1' and not counting:
            counting = True
            current = 1

        elif b == '1' and counting:
            current += 1

    if counting and current > longest_sequence:
        longest_sequence = current

    return longest_sequence


def flip_a_zero_bit(binary):
    """
    Flips a single bit in a binary sequence from 0 to 1 with the overall
    aim of trying to create a sequence with the greatest number of
    sequential 1s

    :param str binary: A sequence of binary 0s and 1s
    :return: A sequence of binary 0s and 1s with a single bit
    flipped from 0 to 1
    :rtype: str
    """
    for i, d in enumerate(binary):
        if d == '0':
            flipped = binary[:i] + '1' + binary[i + 1:]
            yield flipped
