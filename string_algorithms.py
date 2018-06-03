"""
Contains a selection of string and array related algorithms
"""

from collections import Counter
from math import ceil, floor


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


def zero_matrix(matrix):
    """
    If a matrix value is equal to zero, this algorithm zeros out every
    value in its corresponding row and column

    * This implementation's runtime is O(n)
    * Its space complexity is O(n)

    :param list[list[int]] matrix: The provided matrix
    :rtype: list[list[int]]
    """
    # Create a deep copy of the matrix
    zeroed_matrix = [[y for y in x] for x in matrix]

    x_length = len(matrix)
    y_length = len(matrix[0])

    for x in range(x_length):
        for y in range(y_length):

            if matrix[x][y] != 0:
                continue

            for xi in range(x_length):
                zeroed_matrix[xi][y] = 0
            for yi in range(y_length):
                zeroed_matrix[x][yi] = 0

    return zeroed_matrix


def is_rotation(first, second):
    """
    Checks if the provided strings are rotations of each other

    * We know this algorithm enforces both input strings to have the same length of n
    * We know the runtime of the underlying algorithm to find the rotation offset is
    O(n(n - 1) + n(n + 1 - n/2))

    Hence, this implementation's runtime is O(n(n - 1) + n(n + 1 - n/2))

    * We know the algorithm stores the rotated string in a new variable

    Hence, its space complexity is O(n)

    :param str first: The first string
    :param str second: The second string
    :rtype: bool
    """
    if len(first) != len(second):
        raise ValueError("The provided strings need to be the same length")

    offset = find_rotation_offset(first, second)
    rotated = second[offset:] + second[:offset]

    return True if first == rotated else False


def find_rotation_offset(first, second):
    """
    Finds how many right rotations are required to translate the first string
    to the second string

    * We know this algorithm enforces both input strings to have the same length of n
    * We also know the runtime of find_unique_substrings is approximately
      = O(a * (a - 1)/2 * (b - 1)/2)  [which can now be simplified down to]
      = O(n * (n - 1)/2 * (n - 1)/2)
      = O(n * (n - 1))
    * We make the simplistic assumptions that the average number of unique
    substrings returned is equal to n and the average substring length is n/2.
    Therefore, for n substrings, we have (n + 1 - n/2) iterations.

    Hence, This implementation's runtime is approximately O(n(n - 1) + n(n + 1 - n/2))

    * We know for any loop that the algorithm stores the current substring
    which we assume has an average length of n/2

    Therefore, its space complexity is approximately O(n/2)

    :param str first: The first string
    :param str second: The second string
    :return: The number of right rotations to translate the first to the second message
    :rtype: int
    """
    if len(first) != len(second):
        raise ValueError("The provided strings need to be the same length")

    if first == second:
        return 0

    for unique_substring in find_unique_substrings(first, second):
        for i in range(len(second) + 1 - len(unique_substring)):
            if second[i: i + len(unique_substring)] == unique_substring:
                return i

    raise Exception("The two provided strings are not rotated versions of each other")


def find_unique_substrings(first, second):
    """
    For two strings, find the unique substrings that are present only once in
    both strings. In this case, we produce the substrings in order of shortest
    first.

    To calculate the runtime of this algorithm, we define the length the first
    string as 'a' and the length of the second string as 'b'. We can see that
    there are approximately 'a' outer loops, and determine that there are two
    further nested inner loops with an average number of iterations of (a-1)/2
    and (b-1)/2 respectively.

    * This implementation's runtime is approximately O(a * (a-1)/2 * (b-1)/2)
    * Its space complexity is O(1)

    :param str first: The first string
    :param str second: The second string
    :rtype: str
    """
    for unique_character_count in range(1, len(first)):
        for f in range(len(first) + 1 - unique_character_count):
            unique_chars = first[f: f + unique_character_count]

            unique = False
            for k in range(len(second) + 1 - unique_character_count):
                if unique_chars == second[k: k + unique_character_count]:
                    if unique:
                        unique = False
                        break
                    unique = True

            if unique:
                yield unique_chars
