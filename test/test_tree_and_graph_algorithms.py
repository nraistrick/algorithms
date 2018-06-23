import unittest

from tree_and_graph_algorithms import \
    BinaryNode, \
    traverse_binary_tree, \
    traverse_binary_tree_post_order, \
    traverse_binary_tree_pre_order


class TestTreeAndGraphAlgorithms(unittest.TestCase):
    def test_binary_tree_traversal(self):
        """
        Checks we correctly iterate through the values in a binary
        tree in the correct order
        """
        # Set up a binary tree
        tree = BinaryNode(5)
        tree.left = BinaryNode(3)
        tree.left.left = BinaryNode(1)
        tree.left.right = BinaryNode(4)
        tree.right = BinaryNode(9)
        tree.right.left = BinaryNode(6)
        tree.right.right = BinaryNode(10)

        ordered = [v for v in traverse_binary_tree(tree)]
        self.assertEqual([1, 3, 4, 5, 6, 9, 10], ordered)

        pre_ordered = [v for v in traverse_binary_tree_pre_order(tree)]
        self.assertEqual([5, 3, 1, 4, 9, 6, 10], pre_ordered)

        post_ordered = [v for v in traverse_binary_tree_post_order(tree)]
        self.assertEqual([1, 4, 3, 6, 10, 9, 5], post_ordered)

