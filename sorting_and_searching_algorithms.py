"""
Contains a selection of sorting and searching algorithms
"""
import math

from algorithms import are_anagrams


def merge_two_sorted_lists(a, b):
    """
    Merge the sorted list b into a. It's assumed that list a already has
    allocated space for the elements in list b by padding out its values
    with extra None values

    * This implementation's runtime is O(ab)
    * Its space complexity is O(1)

    :param list[int] a: Merge other values into this
    :param list[int] b: The other values
    :rtype: list[int]
    """
    for bidx, bval in enumerate(b):
        inserted = False
        to_move = None
        for aidx, aval in enumerate(a):
            if to_move:
                a[aidx], to_move = to_move, a[aidx]
            elif bval <= aval:
                to_move = aval
                a[aidx] = bval
                inserted = True
            elif aval is None and not inserted:
                a[aidx] = bval
                break

    return a


def sort_by_anagram(unsorted):
    """
    An algorithm to sort a list into groups of anagrams

    * This implementation's runtime is O(ab)
    * Its space complexity is O(1)

    :param list[str] unsorted: An unsorted list of strings
    :return: A sorted list of strings
    :rtype: list[str]
    """
    i = 0
    while i < len(unsorted):
        j = i + 2
        while j < len(unsorted):
            if are_anagrams(unsorted[i], unsorted[j]):
                unsorted[i + 1], unsorted[j] = unsorted[j], unsorted[i + 1]
                break
            j += 1
        i += 1

    return unsorted


def search_in_rotated_array(rotated_array, search_value):
    index = len(rotated_array) / 2
    max_steps = math.log(len(rotated_array), 2) + 1
    steps = 1
    reverse = False

    # We assume here the array is still ordered, but rotated.
    # This check reverses the direction of the binary search to
    # accommodate for the situation where the search value is
    # on the opposite side of the array.
    #
    # e.g. search for 4 in [4, 5, 6, 1, 2, 3]. Our first move here
    # would be to shift the index left instead of right (which would
    # occur in a non-rotated binary tree).
    if search_value > rotated_array[-1]:
        reverse = True

    while True:
        if rotated_array[index] == search_value:
            return index

        index_shift = (len(rotated_array) - 1) / (steps * 2)

        if reverse:
            index_shift *= -1

        if rotated_array[index] > search_value:
            index -= index_shift
        elif rotated_array[index] < search_value:
            index += index_shift
        else:
            raise Exception("This should never happen")

        if steps >= max_steps:
            raise ValueError("Search value {0} not found".format(search_value))

        steps += 1
