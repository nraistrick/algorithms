"""
A collection of generic algorithms for solving various programming tasks
"""


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
