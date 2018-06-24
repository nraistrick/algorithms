import unittest

from tree_and_graph_algorithms import \
    BinaryNode, \
    breadth_first_search, \
    create_binary_tree, \
    create_list_of_depths, \
    depth_first_search, \
    GraphVertex, \
    route_exists, \
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

    def test_route_exists(self):
        """
        Check we correctly identify if a route exists between two
        nodes in a graph
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

        fifth = GraphVertex(5)
        sixth = GraphVertex(6)
        fifth.vertices.append(sixth)
        sixth.vertices.append(fifth)

        self.assertTrue(route_exists(first, second))
        self.assertTrue(route_exists(first, third))
        self.assertTrue(route_exists(third, fourth))
        self.assertTrue(route_exists(fifth, sixth))
        # self.assertTrue(route_exists(first, first))

        self.assertFalse(route_exists(first, fifth))
        self.assertFalse(route_exists(sixth, second))

    def test_create_binary_tree(self):
        """
        Checks we correctly create a minimal height binary tree from a
        collection of sorted integer values
        """
        values = [0, 1, 2]
        tree = create_binary_tree(values)
        self.assertEqual(1, tree.value)
        self.assertEqual(0, tree.left.value)
        self.assertEqual(2, tree.right.value)

        values = [0, 1, 2, 3, 4, 5, 6, 7]
        tree = create_binary_tree(values)
        self.assertEqual(4, tree.value)

        self.assertEqual(2, tree.left.value)
        self.assertEqual(6, tree.right.value)

        self.assertEqual(1, tree.left.left.value)
        self.assertEqual(3, tree.left.right.value)
        self.assertEqual(5, tree.right.left.value)
        self.assertEqual(7, tree.right.right.value)

        self.assertEqual(0, tree.left.left.left.value)

    def test_list_of_depths(self):
        """
        For a given binary tree, tests we correctly create a set of
        linked-lists, each of which represents all the nodes in a single
        layer of the binary tree
        """
        # Set up a binary tree
        tree = BinaryNode(5)
        tree.left = BinaryNode(3)
        tree.left.left = BinaryNode(1)
        tree.left.right = BinaryNode(4)
        tree.right = BinaryNode(9)
        tree.right.left = BinaryNode(6)
        tree.right.right = BinaryNode(10)

        depths = create_list_of_depths(tree)

        self.assertEqual(3, len(depths))
        self.assertEqual(depths[0].value, 5)

        self.assertEqual(depths[1].value, 3)
        self.assertEqual(depths[1].child.value, 9)

        self.assertEqual(depths[2].value, 1)
        self.assertEqual(depths[2].child.value, 4)
        self.assertEqual(depths[2].child.child.value, 6)
        self.assertEqual(depths[2].child.child.child.value, 10)
