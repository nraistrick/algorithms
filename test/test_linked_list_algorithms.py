import unittest

from linked_list_algorithms import \
    delete_middle_node, \
    get_kth_to_last_element, \
    get_unique, \
    get_unique_reverse, \
    Node, \
    remove_duplicates, \
    remove_duplicates_with_sorting, \
    remove_duplicates_without_buffer, \
    sort


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
