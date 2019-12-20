"""
Contains a selection of sorting and searching algorithms
"""


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
