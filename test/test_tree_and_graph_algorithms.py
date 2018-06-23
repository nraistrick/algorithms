import unittest

from tree_and_graph_algorithms import \
    BinaryNode, \
    breadth_first_search, \
    depth_first_search, \
    GraphVertex, \
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

    def test_graph_depth_first_search(self):
        """
        Checks we correctly find values in a graph using a depth-first
        search approach
        """
        # Set up a binary tree
        first = GraphVertex(1)
        second = GraphVertex(2)
        third = GraphVertex(3)
        fourth = GraphVertex(4)

        first.vertices.extend([second, fourth])
        second.vertices.extend([third, fourth])
        third.vertices.append(first)
        fourth.vertices.append(second)

        # Perform searches
        found, vertex, nodes_visited = depth_first_search(first, 1)
        self.assertTrue(found)
        self.assertEqual(1, vertex.value)
        self.assertEqual(1, nodes_visited)

        found, vertex, nodes_visited = depth_first_search(first, 2)
        self.assertTrue(found)
        self.assertEqual(2, vertex.value)
        self.assertEqual(2, nodes_visited)

        found, vertex, nodes_visited = depth_first_search(first, 3)
        self.assertTrue(found)
        self.assertEqual(3, vertex.value)
        self.assertEqual(3, nodes_visited)

        found, vertex, nodes_visited = depth_first_search(first, 4)
        self.assertTrue(found)
        self.assertEqual(4, vertex.value)
        self.assertEqual(3, nodes_visited)

        found, vertex, nodes_visited = depth_first_search(first, 10)
        self.assertFalse(found)
        self.assertIsNone(vertex)
        self.assertIsNone(nodes_visited)

    def test_graph_depth_first_search(self):
        """
        Checks we correctly find values in a graph using a breadth-first
        search approach
        """
        # Set up a directed graph
        first = GraphVertex(1)
        second = GraphVertex(2)
        third = GraphVertex(3)
        fourth = GraphVertex(4)

        first.vertices.extend([second, fourth])
        second.vertices.extend([third, fourth])
        third.vertices.append(first)
        fourth.vertices.append(second)

        # Perform searches
        found, vertex, nodes_visited = breadth_first_search(first, 1)
        self.assertTrue(found)
        self.assertEqual(1, vertex.value)
        self.assertEqual(1, nodes_visited)

        found, vertex, nodes_visited = breadth_first_search(first, 2)
        self.assertTrue(found)
        self.assertEqual(2, vertex.value)
        self.assertEqual(2, nodes_visited)

        found, vertex, nodes_visited = breadth_first_search(first, 3)
        self.assertTrue(found)
        self.assertEqual(3, vertex.value)
        self.assertEqual(4, nodes_visited)

        found, vertex, nodes_visited = breadth_first_search(first, 4)
        self.assertTrue(found)
        self.assertEqual(4, vertex.value)
        self.assertEqual(3, nodes_visited)

        found, vertex, nodes_visited = breadth_first_search(first, 10)
        self.assertFalse(found)
        self.assertIsNone(vertex)
        self.assertIsNone(nodes_visited)

