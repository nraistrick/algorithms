"""
Contains a selection of tree and graph related algorithms
"""


class BinaryNode(object):
    """
    A node that's part of a binary tree
    """
    def __init__(self, value, left=None, right=None):
        """
        :type value: int
        :type left: BinaryNode
        :type right: BinaryNode
        """
        self.value = value
        self.left = left
        self.right = right


def traverse_binary_tree(tree):
    """
    Iterates through and yields binary tree values in order

    :param BinaryNode tree: The root node of the tree
    :return: Values of each node
    :rtype: collections.Iterable[int]
    """
    if not tree:
        return

    for n in traverse_binary_tree(tree.left):
        yield n

    yield tree.value

    for n in traverse_binary_tree(tree.right):
        yield n


def traverse_binary_tree_pre_order(tree):
    """
    Iterates through and yields binary tree values, yielding the value
    of the current node visited first

    :param BinaryNode tree: The root node of the tree
    :return: Values of each node
    :rtype: collections.Iterable[int]
    """
    if not tree:
        return

    yield tree.value

    for n in traverse_binary_tree_pre_order(tree.left):
        yield n

    for n in traverse_binary_tree_pre_order(tree.right):
        yield n


def traverse_binary_tree_post_order(tree):
    """
    Iterates through and yields binary tree values, yielding the value
    of the current node visited last

    :param BinaryNode tree: The root node of the tree
    :return: Values of each node
    :rtype: collections.Iterable[int]
    """
    if not tree:
        return

    for n in traverse_binary_tree_post_order(tree.left):
        yield n

    for n in traverse_binary_tree_post_order(tree.right):
        yield n

    yield tree.value

