import unittest

from tree_and_graph_algorithms import \
    BinaryNode, \
    BinaryNodeWithParent, \
    breadth_first_search, \
    create_binary_tree, \
    create_list_of_depths, \
    depth_first_search, \
    find_build_order, \
    find_max_values, \
    find_min_values, \
    find_successor, \
    get_max_depth, \
    GraphVertex, \
    is_balanced, \
    route_exists, \
    traverse_binary_tree, \
    traverse_binary_tree_post_order, \
    traverse_binary_tree_pre_order, \
    validate_binary_search_tree


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

    def test_get_maximum_depth(self):
        """
        Checks we correctly calculate the maximum depth of a provided
        binary search tree
        """
        first_tree = BinaryNode(1)
        self.assertEqual(1, get_max_depth(first_tree))

        second_tree = BinaryNode(1)
        second_tree.left = BinaryNode(0)
        self.assertEqual(2, get_max_depth(second_tree))

        third_tree = BinaryNode(5)
        third_tree.left = BinaryNode(3)
        third_tree.left.left = BinaryNode(1)
        third_tree.left.right = BinaryNode(4)
        third_tree.right = BinaryNode(9)
        third_tree.right.left = BinaryNode(6)
        self.assertEqual(3, get_max_depth(third_tree))

        fourth_tree = BinaryNode(1)
        fourth_tree.right = BinaryNode(2)
        fourth_tree.right.right = BinaryNode(3)
        fourth_tree.right.right.right = BinaryNode(4)
        self.assertEqual(4, get_max_depth(fourth_tree))

    def test_is_balanced(self):
        """
        Checks if a given binary tree is balanced. A balanced binary tree
        is considered to be a tree which has child branches with a maximum
        difference in depth of one.
        """
        # Set up a balanced binary tree
        balanced_tree = BinaryNode(5)
        balanced_tree.left = BinaryNode(3)
        balanced_tree.left.left = BinaryNode(1)
        balanced_tree.left.right = BinaryNode(4)
        balanced_tree.right = BinaryNode(9)
        balanced_tree.right.left = BinaryNode(6)
        balanced_tree.right.right = BinaryNode(10)

        unbalanced_tree = BinaryNode(3)
        unbalanced_tree.left = BinaryNode(0)
        unbalanced_tree.left.right = BinaryNode(1)
        unbalanced_tree.left.right.right = BinaryNode(2)
        unbalanced_tree.right = BinaryNode(5)
        unbalanced_tree.right.left = BinaryNode(4)
        unbalanced_tree.right.right = BinaryNode(6)

        self.assertTrue(is_balanced(balanced_tree))
        self.assertFalse(is_balanced(unbalanced_tree))

    def test_find_maximum_values(self):
        """
        Checks we incrementally report the discovered maximum values
        in a binary tree
        """
        tree = BinaryNode(3)
        tree.left = BinaryNode(1)
        tree.left.right = BinaryNode(2)
        tree.left.right.right = BinaryNode(4)
        tree.right = BinaryNode(5)
        tree.right.left = BinaryNode(4)
        tree.right.right = BinaryNode(0)

        expected_maximum_values = [3, 4, 5]
        actual_maximum_values = [v for v in find_max_values(tree)]
        self.assertEqual(expected_maximum_values, actual_maximum_values)

    def test_find_minimum_values(self):
        """
        Checks we incrementally report the discovered maximum values
        in a binary tree
        """
        tree = BinaryNode(3)
        tree.left = BinaryNode(1)
        tree.left.right = BinaryNode(2)
        tree.left.right.right = BinaryNode(4)
        tree.right = BinaryNode(5)
        tree.right.left = BinaryNode(4)
        tree.right.right = BinaryNode(0)

        expected_minimum_values = [3, 1, 0]
        actual_minimum_values = [v for v in find_min_values(tree)]
        self.assertEqual(expected_minimum_values, actual_minimum_values)

    def test_validate_binary_search_tree(self):
        """
        Tests if we correctly identify if a binary tree is a valid
        binary-search tree i.e. all elements to the left of the root element
        are smaller in value and all elements to the right are greater than or
        equal in value
        """
        binary_search_tree = BinaryNode(5)
        binary_search_tree.left = BinaryNode(3)
        binary_search_tree.left.left = BinaryNode(1)
        binary_search_tree.left.right = BinaryNode(4)
        binary_search_tree.right = BinaryNode(9)
        binary_search_tree.right.left = BinaryNode(6)
        binary_search_tree.right.right = BinaryNode(10)

        self.assertTrue(validate_binary_search_tree(binary_search_tree))

        not_binary_search_tree = BinaryNode(3)
        not_binary_search_tree.left = BinaryNode(1)
        not_binary_search_tree.left.right = BinaryNode(2)
        not_binary_search_tree.left.right.right = BinaryNode(4)
        not_binary_search_tree.right = BinaryNode(5)
        not_binary_search_tree.right.left = BinaryNode(4)
        not_binary_search_tree.right.right = BinaryNode(0)

        self.assertFalse(validate_binary_search_tree(not_binary_search_tree))

    def test_find_successor(self):
        """
        From a given node, checks we correctly find the next successor node in
        a binary search tree
        """
        first = BinaryNodeWithParent(1)
        second = BinaryNodeWithParent(2)
        third = BinaryNodeWithParent(3)
        fourth = BinaryNodeWithParent(4)
        fifth = BinaryNodeWithParent(5)
        sixth = BinaryNodeWithParent(6)
        seventh = BinaryNodeWithParent(7)

        tree = fourth

        tree.left = second
        tree.left.parent = fourth

        tree.left.left = first
        tree.left.left.parent = second

        tree.left.right = third
        tree.left.right.parent = second

        tree.right = sixth
        tree.right.parent = fourth

        tree.right.left = fifth
        tree.right.left.parent = sixth

        tree.right.right = seventh
        tree.right.right.parent = sixth

        self.assertIs(second, find_successor(first))
        self.assertIs(third, find_successor(second))
        self.assertIs(fourth, find_successor(third))
        self.assertIs(fifth, find_successor(fourth))
        self.assertIs(sixth, find_successor(fifth))
        self.assertIs(seventh, find_successor(sixth))

    def test_find_build_order(self):
        """
        Checks we correctly resolve the build order for a set of projects
        based on the provided dependency links
        """
        projects = ["a", "b", "c", "d", "e", "f"]

        # The first project in the tuple is dependent on the second
        # project being built first
        dependencies = [("d", "a"),
                        ("b", "f"),
                        ("d", "b"),
                        ("a", "f"),
                        ("c", "d")]

        success, build_order = find_build_order(projects, dependencies)
        self.assertTrue(success)
        self.assertEqual(["f", "a", "b", "d", "c", "e"], build_order)

        # Add a circular dependency so it's impossible to successfully
        # build all the projects. The circular dependency here is:
        # b -> d -> c -> b -> ...
        dependencies.append(("b", "c"))

        success, build_order = find_build_order(projects, dependencies)
        self.assertFalse(success)
        self.assertEqual(["f", "a", "e"], build_order)
