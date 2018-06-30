"""
Contains a selection of tree and graph related algorithms
"""

from enum import Enum
from Queue import Queue

from algorithms import permutations
from linked_list_algorithms import Node


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


class BinaryNodeWithParent(object):
    """
    A node that's part of a binary tree that can also have a link back
    to its parent node
    """
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


class BinaryNodeWithDirections(object):
    """
    A node that's part of a binary tree that can also have a pointer
    to describe the location of two other nodes in the tree
    """
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.first_direction = None   # type: NodeDirection
        self.second_direction = None  # type: NodeDirection


class NodeDirection(Enum):
    """
    Describes the location of a child node relative to the current node
    """
    left = 1
    right = 2
    here = 3


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


def traverse_binary_tree_nodes(tree):
    """
    Iterates through and yields binary tree nodes in order

    :param BinaryNode tree: The root node of the tree
    :return: The nodes in value order
    :rtype: collections.Iterable[BinaryNode]
    """
    if not tree:
        return

    for n in traverse_binary_tree_nodes(tree.left):
        yield n

    yield tree

    for n in traverse_binary_tree_nodes(tree.right):
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


def route_exists(first, second):
    """
    Checks if a route exists between two vertices in a directed graph

    :param GraphVertex first: The first vertex
    :param GraphVertex second: The second vertex
    :return: A flag indicating whether a route could be found
    :rtype: bool
    """
    first_queue = Queue()
    first_queue.put(first)
    second_queue = Queue()
    second_queue.put(second)

    first_visited = [first.value]
    second_visited = [second.value]

    while not first_queue.empty() or not second_queue.empty():

        vertices = first_queue.get_nowait().vertices if not first_queue.empty() else []
        for v in vertices:
            if v.value in second_visited:
                return True
            elif v.value in first_visited:
                continue
            else:
                first_visited.append(v.value)
                first_queue.put(v)

        vertices = second_queue.get_nowait().vertices if not second_queue.empty() else []
        for v in vertices:
            if v.value in first_visited:
                return True
            elif v.value in second_visited:
                continue
            else:
                second_visited.append(v.value)
                second_queue.put(v)

    return False


def create_binary_tree(values):
    """
    Creates a minimal-height binary-tree from a list of sorted integer
    elements

    :param list[int] values: A sorted collection of integer values
    :return: The root node of the binary tree
    :rtype: BinaryNode
    """
    if not values or len(values) == 0:
        return

    midpoint = len(values) / 2
    root = BinaryNode(values[midpoint])
    root.left = create_binary_tree(values[:midpoint])
    root.right = create_binary_tree(values[midpoint + 1:])

    return root


def create_list_of_depths(tree):
    """
    Creates a set of linked-lists, each of which contain all the nodes
    in a single layer of a binary-tree

    :param BinaryNode tree: The root node of the tree
    :return: A lookup table, mapping the layer ID to its corresponding linked-list
    :rtype: dict[int, Node]
    """
    if tree is None:
        return {}

    depths = {0: Node(tree.value)}

    further_depths = create_list_of_depths(tree.left)
    for key, value in further_depths.items():
        depths[key + 1] = value

    further_depths = create_list_of_depths(tree.right)
    for key, value in further_depths.items():
        if key + 1 in depths:

            # Add node to the end of the linked-list
            node = depths[key + 1]
            while node.child:
                node = node.child
            node.child = value

        else:
            depths[key + 1] = value

    return depths


def get_max_depth(tree):
    """
    Get's the maximum depth of a binary search tree

    :param BinaryNode tree: The root of a binary tree
    :return: The number of layers in the tree
    :rtype: int
    """
    return 0 if not tree else 1 + max(get_max_depth(tree.left),
                                      get_max_depth(tree.right))


def is_balanced(tree):
    """
    Checks if a binary tree is balanced

    :param BinaryNode tree: A binary tree
    :return: True if the binary tree is balanced, else False
    :rtype: bool
    """
    if not tree:
        return True

    left_depth = get_max_depth(tree.left)
    right_depth = get_max_depth(tree.right)
    if abs(left_depth - right_depth) > 1:
        return False

    return True if is_balanced(tree.left) and is_balanced(tree.right) else False


def find_max_values(tree):
    """
    Iterate through the values in the provided binary tree structure
    and incrementally report the maximum value found. We don't assume
    that the provided tree is a binary-search tree i.e. the tree isn't
    guaranteed to present values in order.

    :param BinaryNode tree: The root of a binary tree
    :return: The latest maximum values as the algorithm iterates through the tree
    :rtype: collections.Iterable[int]
    """
    if not tree:
        raise ValueError("No binary tree provided")

    maximum = tree.value
    yield maximum

    for branch in tree.left, tree.right:

        try:
            for v in find_max_values(branch):
                if v > maximum:
                    maximum = v
                    yield maximum

        except ValueError:
            pass


def find_min_values(tree):
    """
    Iterate through the values in the provided binary tree structure
    and incrementally report the minimum value found. We don't assume
    that the provided tree is a binary-search tree i.e. the tree isn't
    guaranteed to present values in order.

    :param BinaryNode tree: The root of a binary tree
    :return: The latest minimum values as the algorithm iterates through the tree
    :rtype: collections.Iterable[int]
    """
    if not tree:
        raise ValueError("No binary tree provided")

    minimum = tree.value
    yield minimum

    for branch in tree.left, tree.right:

        try:
            for v in find_min_values(branch):
                if v < minimum:
                    minimum = v
                    yield minimum

        except ValueError:
            pass


def validate_binary_search_tree(tree):
    """
    Checks if a binary tree is a valid binary-search tree i.e. all values
    to the left of the root node are smaller in value and all values to the
    right of the root node are equal or larger in value.

    :param BinaryNode tree: The root binary node in the tree
    :return: True if the tree is a valid binary search tree, False otherwise
    :rtype: bool
    """
    if not tree:
        return False

    for v in find_max_values(tree.left):
        if v >= tree.value:
            return False

    for v in find_min_values(tree.right):
        if v < tree.value:
            return False

    return True


def find_successor(current):
    """
    For a binary-search tree, find the next node in sequence after the current

    :param BinaryNodeWithParent current: The current node
    :return: The next node in sequence
    :rtype: BinaryNodeWithParent
    """
    if current.right:
        node = current.right
        while node.left:
            node = node.left
        return node

    else:
        node = current.parent
        while node.value <= current.value:
            if not node.parent:
                raise ValueError("No successor node. Have been provided "
                                 "with the last node in the sequence.")
            node = node.parent

    return node


def find_build_order(projects, dependencies):
    """
    Finds a valid build order for the provided projects, given a list of
    project dependencies

    :param list[str] projects: The project names
    :param list[tuple[str, str]] dependencies: A collection of project
    dependencies. The first project name is dependent on the second project
    being built
    :return: Whether we build the project successfully and the build order
    :rtype: tuple[boolean, list[str]]
    """
    class Project(object):
        """
        Represents a single project to be built
        """
        def __init__(self, name, children=None, parents=None):
            """
            :type name: str
            :type children: list[Project]
            :type parents: list[Project]
            """
            self.name = name
            self.children = children or []
            self.parents = parents or []
            self.built = False

    # Set up a project graph with dependency links
    project_vertices = {p: Project(p) for p in projects}
    for child, parent in dependencies:
        project_vertices[child].parents.append(project_vertices[parent])
        project_vertices[parent].children.append(project_vertices[child])

    # First add projects to the queue that don't have any dependencies
    stack = []
    for p in project_vertices.values():
        if not p.parents:
            stack.append(p)

    # Now try build the remaining projects in an allowable order
    build_order = []
    while stack:
        current = stack.pop(-1)

        parents_built = not any([p for p in current.parents if p.built is False])
        if not parents_built:
            continue

        current.built = True
        build_order.append(current.name)
        for child in current.children:
            stack.append(child)

    # Check if all the projects have been build successfully
    success = not any([p for p in project_vertices.values() if p.built is False])

    return success, build_order


def find_common_ancestor(first, second):
    """
    Finds the first common ancestor between two nodes

    To calculate the runtime of this algorithm, we define the number of
    parents before reaching a common ancestor for the first and second
    nodes to be 'a' and 'b' respectively.

    * This implementation's runtime is O(ab)
    * Its space complexity is O(1)

    :param BinaryNodeWithParent first: The first node
    :param BinaryNodeWithParent second: The second node
    :return: The first common ancestor. If one of the node's in an ancestor
    of the other, return that instead.
    :rtype: BinaryNodeWithParent
    """
    while True:
        current = second
        while True:
            if first is current:
                return first
            elif not current.parent:
                break
            else:
                current = current.parent

        if first.parent:
            first = first.parent
        else:
            break

    raise ValueError("Unable to find common ancestor for provided nodes")


def find_common_ancestor_without_parents(first, second, tree):
    """
    Finds the first common ancestor between two nodes in a tree structure
    where nodes have no links back to their respective parents

    * This implementation's runtime is O(n)
    * Its space complexity is O(n)

    :param BinaryNode first: The first node
    :param BinaryNode second: The second node
    :param BinaryNode tree: The root of a binary tree containing the provided nodes
    :return: The first common ancestor. If one of the node's in an ancestor
    of the other, return that instead.
    :rtype: BinaryNode
    """
    first_left, second_left = False, False
    first_right, second_right = False, False

    if first is tree or second is tree:
        return tree

    for value in traverse_binary_tree_pre_order(tree.left):
        if value == first.value:
            first_left = True
        elif value == second.value:
            second_left = True

    for value in traverse_binary_tree_pre_order(tree.right):
        if value == first.value:
            first_right = True
        elif value == second.value:
            second_right = True

    if first_left and second_left:
        return find_common_ancestor_without_parents(first, second, tree.left)
    elif first_right and second_right:
        return find_common_ancestor_without_parents(first, second, tree.right)
    elif not (first_left or first_right) or not (second_left or second_right):
        raise ValueError("Unable to find both of the nodes in the provided tree")
    else:
        return tree


def find_common_ancestor_with_directions(first, second, tree):
    """
    Finds the first common ancestor between two nodes in a tree structure
    where nodes have no links back to their respective parents. Instead,
    we populate nodes in the tree with directions to the specified nodes
    and use those to locate the first common ancestor.

    :param BinaryNodeWithDirections first: The first node
    :param BinaryNodeWithDirections second: The second node
    :param BinaryNodeWithDirections tree: The root of a binary tree containing the provided nodes
    :return: The first common ancestor. If one of the node's is an ancestor
    of the other, return that instead.
    :rtype: BinaryNodeWithDirections
    """
    first_available, second_available = populate_tree_directions(first, second, tree)

    if not first_available and second_available:
        raise ValueError("Unable to find both of the nodes in the provided tree")

    node = tree
    while node.first_direction == node.second_direction:
        if node.first_direction == NodeDirection.left:
            node = node.left
        elif node.first_direction == NodeDirection.right:
            node = node.right
        elif node.first_direction == NodeDirection.here:
            break
        else:
            raise ValueError("Got unexpected direction instruction."
                             "Check the binary tree was populated correctly.")

    return node


def populate_tree_directions(first, second, tree):
    """
    Populate nodes in the tree with directions to the provided first
    and second nodes

    :param BinaryNodeWithDirections first: The first node
    :param BinaryNodeWithDirections second: The second node
    :param BinaryNodeWithDirections tree: The root of the binary tree
    :return: Two booleans indicating whether the respective first and second
    nodes are available in the current tree
    :rtype: tuple[boolean, boolean]
    """
    # Reset the directions on each node if it's not the one we want
    tree.first_direction = NodeDirection.here if tree is first else None
    tree.second_direction = NodeDirection.here if tree is second else None

    if tree.first_direction is tree.second_direction is NodeDirection.here:
        return True, True

    for branch, direction in (tree.left, NodeDirection.left), (tree.right, NodeDirection.right):
        if not branch:
            continue

        first_found, second_found = populate_tree_directions(first, second, branch)

        if first_found:
            tree.first_direction = direction
        if second_found:
            tree.second_direction = direction

    first_found, second_found = tree.first_direction is not None, tree.second_direction is not None

    return first_found, second_found


def get_tree_levels(tree):
    """
    Attempts to flatten a binary search tree into its individual component
    levels e.g.

    Input
    -----

        4    <--- 1st level
       / \
      2  6   <--- 2nd level
     /\  /\
    1 3 5 7  <--- 3rd level
    ...

    Output
    ------
    [[4], [2, 6], [1, 3, 5, 7] ...]

    :param BinaryNode tree: The root node of a binary search tree
    :return: A collection of layers
    :rtype: list[list[int]]
    """
    if not tree:
        return []

    levels = [[tree.value]]

    further_levels = get_tree_levels(tree.left)
    for l in further_levels:
        levels.append(l)

    further_levels = get_tree_levels(tree.right)
    for i, l in enumerate(further_levels, start=1):
        if i >= len(levels):
            levels.append(l)
        else:
            levels[i].extend(l)

    return levels


def get_tree_creation_values(tree):
    """
    Gets all possible combinations of ordered values that can be
    used to create a binary search tree

    :param BinaryNode tree: The root node of a binary search tree
    :return: All possible permutations of input values that can
    create the provided binary tree when traversed in order e.g.

    Input
    -----

        4    <--- 1st level
       / \
      2  6   <--- 2nd level
     /
    1        <--- 3rd level
    ...

    Output
    ------
    [(4, 2, 6, 1),
     (4, 6, 2, 1),
     (4, 2, 1, 6),
     (4, 2, 6, 1)]

    The parent values of a node, must appear before their respective child
    nodes in the list
    """
    nodes = [n for n in traverse_binary_tree_nodes(tree)]
    dependencies = create_parent_dependencies(tree)

    for p in permutations(nodes):
        inserted = {n: False for n in nodes}
        valid = True
        for node in p:
            inserted[node] = True

            parent = dependencies[node]
            if parent is None:
                continue
            elif inserted[parent] is False:
                valid = False
                break

        if valid:
            yield tuple([node.value for node in p])


def create_parent_dependencies(tree, parent=None):
    """
    Creates a lookup table linking a current node in a binary tree to its
    respective parent node

    :param BinaryNode tree: The root node of the binary tree
    :param BinaryNode parent: The parent node of the provided tree
    :return: A lookup table to find the parent node for any given child
    :rtype: dict[BinaryNode, BinaryNode]
    """
    dependencies = {}
    if not tree:
        return dependencies

    dependencies[tree] = parent

    for branch in tree.left, tree.right:
        further = create_parent_dependencies(branch, tree)
        for k, v in further.items():
            dependencies[k] = v

    return dependencies
