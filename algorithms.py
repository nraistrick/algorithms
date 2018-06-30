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


def permutations(entries):
    """
    An alternative to the itertools.permutations algorithm for getting
    all the possible permutations of a list

    :param list entries: A collection of values
    :return: All possible combinations of the provided values
    :rtype: list
    """
    if not entries:
        return

    if len(entries) == 1:
        yield tuple(entries)
        return

    for i in range(len(entries)):
        remaining = list(entries)
        del remaining[i]

        further = permutations(remaining)
        for f in further:
            permutation = [entries[i]]
            permutation.extend(f)
            yield tuple(permutation)
