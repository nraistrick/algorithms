"""
Contains a selection of linked-list related algorithms
"""


class Node(object):
    """
    Represents a single node in a singly linked-list

    :param int value: The value of the item
    :param Node child: A reference to the next item in the list
    """
    def __init__(self, value, child=None):
        self.value = value
        self.child = child


def remove_duplicates(node):
    """
    Removes all duplicate nodes from an unsorted linked-list. This is
    achieved using a temporary buffer to store previously seen values.

    * This implementation's runtime is O(n)
    * Its space complexity is O(n)

    :param Node node: The head of the linked list
    """
    values_seen = set()
    while node.child:
        if node.child.value in values_seen:
            node.child = node.child.child
        else:
            values_seen.add(node.value)
            node = node.child


def remove_duplicates_without_buffer(node):
    """
    Removes duplicates from an unsorted linked-list without using a temporary
    buffer.

    * This implementation's runtime is O(n^2)
    * Its space complexity is O(1)

    :param Node node: The head of the linked list
    """
    head = node
    while head:
        while node:
            if node.child and node.child.value == head.value:
                node.child = node.child.child
            else:
                node = node.child
        head = head.child
        node = head


def remove_duplicates_with_sorting(node):
    """
    Removes duplicates from an unsorted linked-list without using a temporary
    buffer. This is achieved by first sorting the list. As such a side-effect
    of this algorithm is that we lose the original ordering of the list.

    * This implementation's runtime is O(n^2)
    * Its space complexity is O(1)

    :param Node node: The head of the linked list
    """
    sort(node)
    while node.child:
        if node.value == node.child.value:
            node.child = node.child.child
        else:
            node = node.child


def sort(node):
    """
    Sorts a singly linked-list

    * This implementation's runtime is O(n^2)
    * Its space complexity is O(1)

    :param Node node: The head node of the linked list
    """
    head = node
    while node.child:
        if node.value > node.child.value:
            # Switch the order of the two values and jump back to the start
            node.value, node.child.value = node.child.value, node.value
            node = head
        else:
            node = node.child


def get_unique(node, previous=None):
    """
    Get's all unique nodes in a singly-linked list using a recursive approach.
    For a given value, the first node in the list is kept and all subsequent
    nodes are removed. This uses a hash-table as a temporary buffer for
    previously seen values.

    * This implementation's runtime is O(n)
    * Its space complexity is O(n)

    :param Node node: The head of the linked list
    :param set previous: The values of any previously seen nodes
    :return: The linked list with any duplicates removed
    :rtype: Node
    """
    if previous is None:
        previous = set()

    # Only keep the last node in a list if we've not seen it before
    if not node.child:
        return node if node.value not in previous else None

    # Get all remaining unique nodes in the list
    if node.value not in previous:
        previous.add(node.value)
        node.child = get_unique(node.child, previous)
    else:
        node = get_unique(node.child, previous)

    return node


def get_unique_reverse(node):
    """
    Get's all unique nodes in a singly-linked list using a recursive approach.
    For a given value, the last node in the list is kept and all prior
    nodes are removed.

    * This implementation's runtime is O(n^2)
    * Its space complexity is O(n)

    :param Node node: The head of the linked list
    :return: The linked list with any duplicates removed
    :rtype: Node
    """
    if not node.child:
        return node

    unique = get_unique_reverse(node.child)

    # Check this node is not seen later in the list
    this_node_unique = True
    temp = unique
    while temp:
        if temp.value == node.value:
            this_node_unique = False
            break
        temp = temp.child

    # Only include this node in the list if it doesn't have a child
    # with the same value
    if this_node_unique:
        node.child = unique
        return node
    else:
        return unique


def get_kth_to_last_element(node, k):
    """
    Get's the kth to last element in a linked list

    * This implementation's runtime is O(n)
    * Its space complexity is O(1)

    :param Node node: The head of a linked list
    :param int k: The kth to last element
    :return: The kth to last node
    :rtype: Node
    """
    if node is None:
        raise ValueError("Must be passed a valid linked-list")

    head = node
    length = 0

    while node:
        length += 1
        node = node.child

    element_to_find = length - k - 1
    node = head

    while element_to_find:
        node = node.child
        element_to_find -= 1

    return node
