"""
A collection of generic algorithms for solving various programming tasks
"""

from collections import Counter
from math import ceil, floor


def find_sum_combinations(total, components, created=0):
    """
    Finds all combinations of numbers which sum to a specified total

    * This implementation's runtime is O(n!)
    * Its space complexity is O(n!)

    :param int total: The total the numbers should sum to
    :param int components: How many numbers should be added together to create the total
    :param int created: How many numbers have been generated so far
    :return: All possible numbers combinations for the provided total
    :rtype: list[list[int]]
    """
    if components < 2:
        raise ValueError("Need to divide the total between at least two numbers")

    one_component_remaining = (components - created == 1)
    if one_component_remaining:
        return [[total]]

    combinations = []
    for i in range(0, total + 1):
        further_sequences = find_sum_combinations(total - i, components, created + 1)

        for sequence in further_sequences:
            combinations.append([i] + sequence)

    return combinations


def all_unique_characters(text):
    """
    Checks if all characters in a provided string are unique

    * This implementation's runtime is O(n)
    * Its space complexity is O(n)

    :param str text: A provided input string
    :rtype: bool
    """
    if len(text) == len(set(text)):
        return True
    return False


def all_unique_characters_with_loop(text):
    """
    Checks if all characters in a provided string are unique

    * This implementation's runtime is O(n^2)
    * Its space complexity is O(1)

    :param str text: A provided input string
    :rtype: bool
    """
    for i in range(0, len(text)):
        for j in range(0, len(text)):
            if j == i:
                continue
            elif text[i] == text[j]:
                return False

    return True


def is_permutation(first, second):
    """
    Checks if the provided strings are permutations of each other
    i.e. they contain the same characters, but in a different order

    If we define the length the first string as 'a' and the length of the
    second string as 'b':
    * This implementation's runtime is O(ab)
    * Its space complexity is O(b)

    :param str first: The first string
    :param str second: The second string
    :rtype: bool
    """
    characters = list(second)

    for c in first:
        if c not in characters:
            return False
        characters.remove(c)

    remaining_characters = (len(characters) != 0)
    if remaining_characters:
        return False

    return True


def is_permutation_with_inner_loop(first, second):
    """
    Checks if the provided strings are permutations of each other
    i.e. they contain the same characters, but in a different order

    If we define the length the first string as 'a' and the length of the
    second string as 'b':
    * This implementation's runtime is O(ab)
    * Its space complexity is O(b)

    :param str first: The first string
    :param str second: The second string
    :rtype: bool
    """
    characters = list(second)

    for c in first:
        exists = False
        for sc in characters:
            if c == sc:
                exists = True
                characters.remove(c)
                break

        if not exists:
            return False

    remaining_characters = (len(characters) != 0)
    if remaining_characters:
        return False

    return True


def url_encode(text, length):
    """
    URL encodes spaces in a provided string. The string includes whitespace
    appended to allow for expansion without dynamic array resizing. The length
    of the original string is provided.

    Given we know length is directly proportional to the provided text:
    * This implementation's runtime is O(n^2)
    * Its space complexity is O(1)

    :param str text: The string which contains spaces to URL encode
    :param int length: The length of the original string
    :return: The URL-encoded string
    :rtype: str
    """
    url_encoded_space = "%20"

    characters = list(text)

    for i in range(0, len(text)):
        if characters[i].isspace():
            for j in range(length - 1, i, -1):
                characters[j + 2] = characters[j]
            characters[i: i + len(url_encoded_space)] = list(url_encoded_space)
            length += 2

    return "".join(characters)


def url_encode_pythonic(text):
    """
    URL encodes spaces in a provided string

    * This implementation's runtime is O(n)
    * Its space complexity is O(1)

    :param str text: The string which contains spaces to URL encode
    :return: The URL-encoded string
    :rtype: str
    """
    return text.replace(" ", "%20")


def has_palindromic_permutation(text):
    """
    Checks if a provided string has a permutation which is a palindrome.

    * This implementation's runtime is O(n)
    * Its space complexity is O(n)

    :param str text: The input string
    :rtype: bool
    """
    # Ignore any spaces that are part of the string
    text = text.replace(" ", "")

    # Get character counts for every letter in the string
    character_counts = Counter(text)

    # For an even length string, every character must be in a pair.
    # For an uneven length string, we can only have one single character
    # which is not part of a pair.
    single_character_allowed = (len(text) % 2 != 0)

    for v in character_counts.values():
        uneven_count = (v % 2 != 0)

        if uneven_count and single_character_allowed:
            single_character_allowed = False

        elif uneven_count:
            return False

    return True


def are_similar(first, second):
    """
    Checks if two strings are the same or have at most one difference. The
    difference can be a single extra/removed character or a differing character.

    For the typical use case, we assume that the provided strings with have
    approximately the same length of n. This allows us to estimate the
    runtime.

    * This implementation's runtime is O(n)
    * Its space complexity is O(1)

    :param str first: The first string
    :param str second: The second string
    :rtype: bool
    """
    i = j = 0
    max_i = len(first) - 1
    max_j = len(second) - 1
    difference_found = False

    while True:
        # Check to see if we've successfully reached the end of both strings
        if i > max_i and j > max_j:
            break

        # Adjust for additional characters at the end of the string
        elif i > max_i:
            i -= 1
        elif j > max_j:
            j -= 1

        # Note the slice allows us to request a value at a
        # non-existent index without throwing an exception
        if first[i: i + 1] != second[j: j + 1]:
            if difference_found:
                return False

            difference_found = True

            # Handle the situation where an extra character has been added
            # or removed. Try adjust the pointers so they are referencing
            # matching characters for the next iteration.
            if j < max_j and first[i] == second[j + 1]:
                j += 1
                continue
            elif i < max_i and first[i + 1] == second[j]:
                i += 1
                continue

        i += 1
        j += 1

    return True


def compress(text):
    """
    Compresses a string with repeated characters into a simple
    compression format using character counts e.g.

    >>> compress("aabbbcccc") == "a2b3c4"

    * This implementation's runtime is O(n)
    * Its space complexity is O(n)

    :param str text: The string to be compressed
    :return: The compressed string
    :rtype: str
    """
    components = []
    current = None
    count = 0

    for c in text:
        if not current:
            current = c

        if c == current:
            count += 1
        else:
            components.append(current + str(count))
            current = c
            count = 1

    components.append(current + str(count))
    compressed = "".join(components)

    # Only return the compressed string if it's actually shorter
    return compressed if len(compressed) < len(text) else text


def rotate_clockwise(image):
    """
    Rotates an image 90 degrees clockwise

    * This implementation's runtime is O(n)
    * Its space complexity is O(n)

    :param list[list[int]] image: The provided square image
    :return: The rotated image
    :rtype: list[list[int]]
    """
    x_max = len(image)
    y_max = len(image[0])
    rotated = [[0 for _ in range(0, x_max)] for _ in range(0, y_max)]

    for x in range(0, x_max):
        for y in range(0, y_max):
            rotated[y_max - 1 - y][x] = image[x][y]

    return rotated


def rotate_clockwise_in_place(image):
    """
    Rotates a square image 90 degrees clockwise without creating
    a brand new image

    To complete this operation, we work under the principle that pixels
    in a square image work in groups of four during rotation. For example,
    let's say we have an 3x3 image of pixels, where each pixel is marked
    as its respective (x, y) coordinate.

                        x
      +----------------->
      | (0,0) (1,0) (2,0)
      |
      | (0,1) (1,1) (2,1)
      |
    y V (0,2) (1,2) (2,2)

    When rotating this image by 90 degrees, there are two main loops that can
    be identified. Each of these loops represents the next location of the
    previous pixel

          Loop 1
          +-------------------+
          |                   |
    +---(0,0)     (1,0)     (2,0)---+
    |             |   |             |
    |     Loop 2  |   |             |
    |     +-------+   +-------+     |
    |     |                   |     |
    |   (0,1)     (1,1)     (2,1)   |
    |     |                   |     |
    |     +-------+   +-------+     |
    |             |   |             |
    |             |   |             |
    +---(0,2)     (1,2)     (2,2)---+
          |                   |
          +-------------------+

    The aim of this method is to identify a starting pixel from each of the
    unique loops, and then rotate the pixels within each loop. In this case,
    the two starting pixels would be (0,0) and (0,1).

    * This implementation's runtime is O(n)
    * Its space complexity is O(1)

    :param list[list[int]] image: The provided square image
    :return: The rotated image
    :rtype: list[list[int]]
    """
    x_max = len(image)
    y_max = len(image[0])

    x_starting_pixels = int(ceil(x_max/2))
    y_starting_pixels = int(floor(y_max/2))
    pixels_per_loop = 4

    # Iterate through all the possible starting pixels
    for x in range(0, x_starting_pixels):
        for y in range(0, y_starting_pixels):

            current_x, current_y = x, y
            temp = None

            # Rotate each pixel in an identified loop
            for _ in range(0, pixels_per_loop):
                next_x, next_y = (y_max - 1 - current_y), current_x
                if temp is None:
                    temp = image[next_x][next_y]
                    image[next_x][next_y] = image[current_x][current_y]
                else:
                    temp, image[next_x][next_y] = image[next_x][next_y], temp

                current_x, current_y = next_x, next_y

    return image
