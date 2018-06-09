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


class DoubleNode(object):
    """
    Represents a single node in a doubly linked-list

    :param int value: The value of the item
    :param Node child: A reference to the next item in the list
    :param Node parent: A reference to the last item in the list
    """
    def __init__(self, value, child=None, parent=None):
        self.value = value
        self.child = child
        self.parent = parent


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


def delete_middle_node(node):
    """
    Removes the middle node from a singly linked-list

    * This implementation's runtime is O(n)
    * Its space complexity is O(1)

    :param Node node: The head of the linked-list
    """
    if not node.child or not node.child.child:
        raise ValueError("Provided linked-list must have 3 or more elements")

    head = node
    node = node.child.child
    while node:
        node = node.child
        if node and node.child:
            node = node.child
            head = head.child

    head.child = head.child.child


def partition_list(node, value):
    """
    Partitions a singly-linked list around a specific value so that the
    left half of the list contains values smaller than the provided value and
    the right half of the list contains values bigger than the provided value

    * This implementation's runtime is O(n^2)
    * Its space complexity is O(1)

    :param Node node: The head of the linked-list
    :param int value: The value to partition around
    """
    head = node
    while node.child:
        if node.value >= value > node.child.value:
            node.value, node.child.value = node.child.value, node.value
            node = head
        else:
            node = node.child


def sum_reverse_numbers(first, second):
    """
    Sums two numbers represented by linked-lists. Each node in a list
    represents a single digit in base 10 number with the least significant
    digit coming first.

    * This implementation's runtime is O(n)
    * Its space complexity is O(1)

    :param Node first: The head node of the first number
    :param second: The head node of the second number
    :return: The summed number as a linked-list
    :rtype: Node
    """
    first_number = get_reverse_number(first)
    second_number = get_reverse_number(second)
    result = first_number + second_number

    return create_reverse_number(result)


def create_reverse_number(value):
    """
    Creates a linked-list representation of a number. The least significant
    digit comes first.

    * This implementation's runtime is O(n)
    * Its space complexity is O(1)

    :param int value: The provided number
    :return: A linked-list representation of the number
    :rtype: Node
    """
    if value <= 0:
        raise ValueError("Must be given a value that's greater than 0")

    # Break the value down into its digits
    base = 10
    digits = []
    while True:
        digits.append(value % base)
        value /= base
        if value == 0:
            break

    # Create a linked list from the digits
    head = node = Node(digits[0])
    for d in digits[1:]:
        node.child = Node(d)
        node = node.child

    return head


def get_reverse_number(node):
    """
    Get's a number from a singly-linked list where each node represents
    a single digit in a base 10 number. The least significant digit comes
    first.

    * This implementation's runtime is O(n)
    * Its space complexity is O(1)

    :param Node node: The head of the linked-list
    :return: The actual value
    :rtype: int
    """
    total = 0
    multiple = 1
    while node:
        total += node.value * multiple
        multiple *= 10
        node = node.child

    return total


def sum_numbers(first, second):
    """
    Sums two numbers represented by linked-lists. Each node in a list
    represents a single digit in base 10 number with the most significant
    digit coming first.

    * This implementation's runtime is O(n)
    * Its space complexity is O(1)

    :param Node first: The head node of the first number
    :param second: The head node of the second number
    :return: The summed number as a linked-list
    :rtype: Node
    """
    first_number = get_number(first)
    second_number = get_number(second)
    result = first_number + second_number

    return create_number(result)


def create_number(value):
    """
    Creates a linked-list representation of a number. The most significant
    digit comes first.

    * This implementation's runtime is O(n)
    * Its space complexity is O(1)

    :param int value: The provided number
    :return: A linked-list representation of the number
    :rtype: Node
    """
    if value <= 0:
        raise ValueError("Must be given a value that's greater than 0")

    # Break the value down into its digits
    base = 10
    digits = []
    while True:
        digits.append(value % base)
        value /= base
        if value == 0:
            break

    # Create a linked list from the digits
    head = node = Node(digits[-1])
    for d in digits[-2::-1]:
        node.child = Node(d)
        node = node.child

    return head


def get_number(node):
    """
    Get's a number from a singly-linked list where each node represents
    a single digit in a base 10 number. The most significant digit comes
    first.

    * This implementation's runtime is O(n)
    * Its space complexity is O(1)

    :param Node node: The head of the linked-list
    :return: The actual value
    :rtype: int
    """
    head = node

    digits = 1
    while node.child:
        node = node.child
        digits += 1

    node = head
    total = 0
    multiple = 10 ** (digits - 1)

    while node:
        total += node.value * multiple
        multiple /= 10
        node = node.child

    return total


def is_palindrome(node):
    """
    Checks if a singly linked-list has a palindromic set of values

    * This implementation's runtime is O(n^2)
    * Its space complexity is O(1)

    :param Node node: The head node
    :return: Whether the list is a palindrome
    :rtype: bool
    """
    # Find length and midpoint of linked-list
    normal = fast = node
    length = 1

    while True:
        if fast and fast.child:
            normal = normal.child
            fast = fast.child.child
            length += 2 if fast else 1
        else:
            break

    midpoint = normal.child if length > 1 and length % 2 == 1 else normal

    # Check if the list is a palindrome
    palindrome = True
    for i in range(length/2):
        mirrored = midpoint
        for _ in range(1, length/2 - i):
            mirrored = mirrored.child

        if node.value != mirrored.value:
            palindrome = False
            break

        node = node.child

    return palindrome


def is_palindrome_using_list(node):
    """
    Checks if a singly linked-list has a palindromic set of values

    * This implementation's runtime is O(n)
    * Its space complexity is O(n)

    :param Node node: The head node
    :return: Whether the list is a palindrome
    :rtype: bool
    """
    data = []
    while node:
        data.append(node.value)
        node = node.child

    for i in range(len(data)/2):
        if data[i] != data[-1 - i]:
            return False

    return True


def is_palindrome_doubly(node):
    """
    Checks if a doubly linked-list has a palindromic set of values

    * This implementation's runtime is O(n)
    * Its space complexity is O(1)

    :param DoubleNode node: The head node
    :return: Whether the list is a palindrome
    :rtype: bool
    """
    length = 1
    end = node
    while end.child:
        end = end.child
        length += 1

    palindrome = True
    for _ in range(length/2):
        if node.value != end.value:
            palindrome = False
            break
        else:
            node = node.child
            end = end.parent

    return palindrome
