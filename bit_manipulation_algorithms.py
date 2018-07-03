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
