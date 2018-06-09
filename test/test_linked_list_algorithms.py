import unittest

from linked_list_algorithms import \
    create_number, \
    create_reverse_number, \
    delete_middle_node, \
    DoubleNode, \
    get_kth_to_last_element, \
    get_number, \
    get_reverse_number, \
    get_unique, \
    get_unique_reverse, \
    is_palindrome, \
    is_palindrome_doubly, \
    is_palindrome_using_list, \
    lists_intersect, \
    lists_intersect_simplistic, \
    Node, \
    partition_list, \
    remove_duplicates, \
    remove_duplicates_with_sorting, \
    remove_duplicates_without_buffer, \
    sort, \
    sum_numbers, \
    sum_reverse_numbers


class TestLinkedListAlgorithms(unittest.TestCase):
    def test_remove_duplicates(self):
        """
        Checks that duplicates are removed correctly from an unsorted
        singly linked-list
        """
        duplicate_values = (1, 0, 1, 3, 6, 1, 1)
        duplicates_removed = (1, 0, 3, 6)

        head = self.create_linked_list(duplicate_values)
        remove_duplicates(head)

        # Confirm duplicates are removed successfully
        self.verify_linked_list_values(head, duplicates_removed)

    def test_remove_duplicates_without_buffer(self):
        """
        Checks that duplicates are removed correctly from an unsorted
        singly linked-list, without the use of a temporary buffer.
        """
        duplicate_values = (1, 0, 1, 3, 6, 1, 1)
        duplicates_removed = (1, 0, 3, 6)

        head = self.create_linked_list(duplicate_values)
        remove_duplicates_without_buffer(head)

        self.verify_linked_list_values(head, duplicates_removed)

    def test_remove_duplicates_with_sorting(self):
        """
        Checks that duplicates are removed correctly from an unsorted
        singly linked-list. In this case, the list is first sorted, making
        it possible to remove duplicates without the requirement for a
        temporary buffer. As a trade-off, we lose the original ordering
        of the list.
        """
        duplicate_values = (1, 0, 1, 3, 6, 1, 1)
        duplicates_removed = (0, 1, 3, 6)

        head = self.create_linked_list(duplicate_values)
        remove_duplicates_with_sorting(head)

        self.verify_linked_list_values(head, duplicates_removed)

    def test_sort_singly_linked_list(self):
        """
        Checks we correctly sort a singly linked-list
        """
        unsorted_values = (4, 3, 5, 1, 2)
        sorted_values = (1, 2, 3, 4, 5)

        head = self.create_linked_list(unsorted_values)
        sort(head)

        self.verify_linked_list_values(head, sorted_values)

    def test_get_unique(self):
        """
        Checks that duplicates are removed correctly from an unsorted
        singly linked-list. For a given value, the first node in the
        list is kept and all subsequent nodes are removed.
        """
        duplicate_values = (1, 0, 1, 3, 6, 1, 1)
        duplicates_removed = (1, 0, 3, 6)

        head = self.create_linked_list(duplicate_values)
        head = get_unique(head)

        self.verify_linked_list_values(head, duplicates_removed)

    def test_get_unique_reverse(self):
        """
        Checks that duplicates are removed correctly from an unsorted
        singly linked-list. For a given value, the last node in the
        list is kept and all previous nodes are removed.
        """
        duplicate_values = (1, 0, 1, 3, 6, 1, 1)
        duplicates_removed = (0, 3, 6, 1)

        head = self.create_linked_list(duplicate_values)
        head = get_unique_reverse(head)

        self.verify_linked_list_values(head, duplicates_removed)

    def test_get_kth_to_last_element(self):
        """
        Checks we can correctly get the kth to last element from a
        singly linked-list
        """
        values = (1, 2, 3, 4, 5)

        head = self.create_linked_list(values)

        available_elements = len(values)
        for i in range(available_elements):
            element = get_kth_to_last_element(head, i)
            self.assertEqual(values[available_elements - i - 1], element.value)

    def test_delete_middle_node(self):
        """
        Checks we correctly delete the middle node of a singly linked-list
        """
        values = 1,
        head = self.create_linked_list(values)
        self.assertRaises(ValueError, delete_middle_node, head)

        values = (1, 2)
        head = self.create_linked_list(values)
        self.assertRaises(ValueError, delete_middle_node, head)

        values = (1, 2, 3)
        expected_values = (1, 3)
        head = self.create_linked_list(values)
        delete_middle_node(head)
        self.verify_linked_list_values(head, expected_values)

        values = (1, 2, 3, 4, 5, 6, 7, 8)
        expected_values = (1, 2, 3, 5, 6, 7, 8)
        head = self.create_linked_list(values)
        delete_middle_node(head)
        self.verify_linked_list_values(head, expected_values)

    def test_partition_list(self):
        """
        Checks we correctly partition a list into two halves based around
        a specific value
        """
        values = (3, 5, 8, 5, 10, 2, 1)
        expected_values = (3, 2, 1, 5, 8, 5, 10)
        head = self.create_linked_list(values)
        partition_list(head, 5)
        self.verify_linked_list_values(head, expected_values)

    def test_sum_reverse_numbers(self):
        """
        Checks we correctly sum together two numbers that are represented by
        singly linked-lists with each node representing a single digit of
        the number. The least significant digit comes first.
        """
        first = self.create_linked_list((7, 1, 6))
        second = self.create_linked_list((5, 9, 2))
        self.verify_linked_list_values(sum_reverse_numbers(first, second), (2, 1, 9))

    def test_get_reverse_number(self):
        """
        Checks we can recreate a number from a linked-list of values
        in reverse digit order
        """
        values = (7, 1, 6)
        head = self.create_linked_list(values)
        self.assertEqual(617, get_reverse_number(head))

        values = (5, 9, 2)
        head = self.create_linked_list(values)
        self.assertEqual(295, get_reverse_number(head))

    def test_create_reverse_number(self):
        """
        Checks we can successfully turn a number into its equivalent linked
        list representation where each node contains one digit of the number
        in base 10. The least significant digit comes first.
        """
        self.assertRaises(ValueError, create_reverse_number, 0)

        expected_values = (2, 1, 9)
        head = create_reverse_number(912)
        self.verify_linked_list_values(head, expected_values)

    def test_sum_numbers(self):
        """
        Checks we correctly sum together two numbers that are represented by
        singly linked-lists with each node representing a single digit of
        the number. The least significant digit comes first.
        """
        first = self.create_linked_list((6, 1, 7))
        second = self.create_linked_list((2, 9, 5))
        self.verify_linked_list_values(sum_numbers(first, second), (9, 1, 2))

    def test_get_number(self):
        """
        Checks we can recreate a number from a linked-list of values
        in normal digit order
        """
        values = (6, 1, 7)
        head = self.create_linked_list(values)
        self.assertEqual(617, get_number(head))

        values = (2, 9, 5)
        head = self.create_linked_list(values)
        self.assertEqual(295, get_number(head))

    def test_create_number(self):
        """
        Checks we can successfully turn a number into its equivalent linked
        list representation where each node contains one digit of the number
        in base 10. The most significant digit comes first.
        """
        self.assertRaises(ValueError, create_number, 0)

        expected_values = (9, 1, 2)
        head = create_number(912)
        self.verify_linked_list_values(head, expected_values)

    def test_is_palindrome(self):
        """
        Checks we correctly identify linked-lists which are also palindromes
        """
        self.assertTrue(is_palindrome(self.create_linked_list((1,))))
        self.assertTrue(is_palindrome(self.create_linked_list((1, 2, 2, 1))))
        self.assertTrue(is_palindrome(self.create_linked_list((1, 2, 3, 2, 1))))

        self.assertFalse(is_palindrome(self.create_linked_list((1, 2))))
        self.assertFalse(is_palindrome(self.create_linked_list((1, 2, 3, 4))))
        self.assertFalse(is_palindrome(self.create_linked_list((1, 2, 3, 2, 2))))

    def test_is_palindrome_using_list(self):
        """
        Checks we correctly identify linked-lists which are also palindromes
        """
        self.assertTrue(is_palindrome_using_list(self.create_linked_list((1,))))
        self.assertTrue(is_palindrome_using_list(self.create_linked_list((1, 2, 2, 1))))
        self.assertTrue(is_palindrome_using_list(self.create_linked_list((1, 2, 3, 2, 1))))

        self.assertFalse(is_palindrome_using_list(self.create_linked_list((1, 2))))
        self.assertFalse(is_palindrome_using_list(self.create_linked_list((1, 2, 3, 4))))
        self.assertFalse(is_palindrome_using_list(self.create_linked_list((1, 2, 3, 2, 2))))

    def test_is_palindrome_doubly(self):
        """
        Checks we correctly identify doubly linked-lists which are also palindromes
        """
        self.assertTrue(is_palindrome_doubly(self.create_linked_list_doubly((1,))))
        self.assertTrue(is_palindrome_doubly(self.create_linked_list_doubly((1, 2, 2, 1))))
        self.assertTrue(is_palindrome_doubly(self.create_linked_list_doubly((1, 2, 3, 2, 1))))

        self.assertFalse(is_palindrome_doubly(self.create_linked_list_doubly((1, 2))))
        self.assertFalse(is_palindrome_doubly(self.create_linked_list_doubly((1, 2, 3, 4))))
        self.assertFalse(is_palindrome_doubly(self.create_linked_list_doubly((1, 2, 3, 2, 2))))

    def test_lists_intersect(self):
        """
        Check if the same node appears in both lists
        """
        first = self.create_linked_list((1, 2, 3))
        second = self.create_linked_list((5, 6, 7))

        self.assertIsNone(lists_intersect(first, second))

        intersecting_node = second.child.child
        temp = first.child.child
        first.child = intersecting_node
        first.child.child = temp

        self.assertEqual(intersecting_node, lists_intersect(first, second))

    def test_lists_intersect_simplistic(self):
        """
        Check if the same node appears in both lists
        """
        first = self.create_linked_list((1, 2, 3))
        second = self.create_linked_list((5, 6, 7))

        self.assertIsNone(lists_intersect_simplistic(first, second))

        intersecting_node = second.child.child
        temp = first.child.child
        first.child = intersecting_node
        first.child.child = temp

        self.assertEqual(intersecting_node, lists_intersect_simplistic(first, second))

    @staticmethod
    def create_linked_list(values):
        """
        Creates a linked list from the provided iterable of values

        :param collections.Iterable values: A collection of node values
        :return: The head of the created linked list
        :rtype: Node
        """
        current = head = Node(values[0])
        for i in values[1:]:
            current.child = Node(i)
            current = current.child

        return head

    @staticmethod
    def create_linked_list_doubly(values):
        """
        Creates a doubly linked list from the provided iterable of values

        :param collections.Iterable values: A collection of node values
        :return: The head of the created linked list
        :rtype: DoubleNode
        """
        current = head = DoubleNode(values[0])
        for i in values[1:]:
            current.child = DoubleNode(i)
            current.child.parent = current
            current = current.child

        return head

    def verify_linked_list_values(self, head, values):
        """
        Checks the values in the provided linked-list match those in the
        provided collection

        :param Node head: The head of a linked-list
        :param tuple values: A collection of node values
        """
        for i in range(len(values)):
            self.assertEqual(values[i], head.value)
            if not head.child:
                break
            head = head.child
