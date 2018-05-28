"""
A collection of generic algorithms for solving various programming tasks
"""

from collections import Counter


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

