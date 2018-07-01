"""
Contains a selection of bit manipulation related algorithms
"""


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
