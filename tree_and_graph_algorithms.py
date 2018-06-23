"""
Contains a selection of tree and graph related algorithms
"""

from Queue import Queue


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


class GraphVertex(object):
    def __init__(self, value, vertices=None):
        """
        Represents a single vertex in a graph

        :param int value: The value of the vertex
        :param list[GraphVertex] vertices: A collection of other vertices that
        are accessible from this vertex by an edge
        """
        self.value = value
        self.vertices = vertices if vertices else []


def depth_first_search(vertex, value, visited=None):
    """
    Perform a depth first search through a directed graph

    :param GraphVertex vertex: The start vertex in the graph
    :param int value: The value to search for
    :param list[int] visited: A collection of previous values visited
    :return: A boolean describing whether the vertex was found, the vertex itself,
    and the number of nodes visited to find the specified node
    :rtype: tuple[boolean, GraphVertex, int]
    """
    if vertex.value == value:
        nodes_visited = len(visited) + 1 if visited else 1
        return True, vertex, nodes_visited

    if visited is None:
        visited = []

    for v in vertex.vertices:
        if v.value in visited:
            continue

        updated_visited = [vertex.value]
        updated_visited.extend(visited)

        found, found_vertex, nodes_visited = depth_first_search(v, value, updated_visited)
        if found:
            return found, found_vertex, nodes_visited

    return False, None, len(visited)


def breadth_first_search(vertex, value):
    """
    Perform a breadth first search through a directed graph

    :param GraphVertex vertex: The start vertex in the graph
    :param int value: The value to search for
    :return: A boolean describing whether the vertex was found, the vertex itself,
    and the number of nodes traversed to find the specified node
    :rtype: tuple[boolean, GraphVertex, int]
    """
    queue = Queue()
    queue.put((vertex, []))

    while not queue.empty():

        vertex, visited = queue.get()
        if vertex.value in visited:
            continue
        elif vertex.value == value:
            return True, vertex, len(visited) + 1

        visited.append(vertex.value)

        for v in vertex.vertices:
            queue.put((v, visited))

    return False, None, None
