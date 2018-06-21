import unittest

from stack_queue_algorithms import \
    MinStack, \
    MultiStack


class TestStackQueueAlgorithms(unittest.TestCase):
    def test_multi_stack_invalid_stack(self):
        """
        Checks we can't push entries onto non-existent stacks
        """
        stack = MultiStack(2)
        self.assertRaises(ValueError, stack.push, 2, "test")
        self.assertRaises(ValueError, stack.push, 3, "test")
        self.assertRaises(ValueError, stack.push, 4, "test")

    def test_multi_stack_empty(self):
        """
        Checks each empty stack responds correctly to requests
        """
        stack = MultiStack(3)

        self.assertItemsEqual([0, 0, 0], stack.entries)

        self.assertRaises(ValueError, stack.pop, 0)
        self.assertRaises(ValueError, stack.pop, 1)
        self.assertRaises(ValueError, stack.pop, 2)
        self.assertRaises(ValueError, stack.pop, 3)
        self.assertRaises(ValueError, stack.pop, 10)

        self.assertRaises(ValueError, stack.push, 3, "blah")
        self.assertRaises(ValueError, stack.push, 10, "blah")

    def test_multi_stack_one_stack(self):
        """
        Checks the multi-stack model performs correctly with one stack
        """
        stack = MultiStack(1)

        stack.push(0, "this")
        stack.push(0, "is")
        stack.push(0, "pizza")
        stack.push(0, "with")
        stack.push(0, "cheese")

        self.assertEqual("cheese", stack.pop(0))
        self.assertEqual("with", stack.pop(0))
        self.assertEqual("pizza", stack.pop(0))
        self.assertEqual("is", stack.pop(0))
        self.assertEqual("this", stack.pop(0))
        self.assertRaises(ValueError, stack.pop, 0)

        self.assertItemsEqual([0], stack.entries)

    def test_multi_stack_two_stacks(self):
        """
        Checks the multi-stack model performs correctly with two stacks
        """
        stack = MultiStack(2)

        stack.push(1, "abc")
        stack.push(0, "this")
        stack.push(0, "is")
        stack.push(1, "def")
        stack.push(0, "pizza")
        stack.push(0, "with")
        stack.push(1, "ghi")
        stack.push(0, "cheese")

        self.assertEqual("ghi", stack.pop(1))
        self.assertEqual("def", stack.pop(1))
        self.assertEqual("abc", stack.pop(1))
        self.assertRaises(ValueError, stack.pop, 1)

        self.assertEqual("cheese", stack.pop(0))
        self.assertEqual("with", stack.pop(0))
        self.assertEqual("pizza", stack.pop(0))
        self.assertEqual("is", stack.pop(0))
        self.assertEqual("this", stack.pop(0))
        self.assertRaises(ValueError, stack.pop, 0)

        self.assertItemsEqual([0, 0], stack.entries)

    def test_multi_stack_three_stacks(self):
        """
        Checks the multi-stack model performs correctly with three stacks
        """
        stack = MultiStack(3)

        stack.push(1, "abc")
        stack.push(0, "this")
        stack.push(0, "is")
        stack.push(1, "def")
        stack.push(2, 135678)
        stack.push(2, 99)
        stack.push(0, "pizza")
        stack.push(0, "with")
        stack.push(0, "cheese")

        self.assertEqual("def", stack.pop(1))
        self.assertEqual("abc", stack.pop(1))
        self.assertRaises(ValueError, stack.pop, 1)

        self.assertEqual("cheese", stack.pop(0))
        self.assertEqual("with", stack.pop(0))
        self.assertEqual("pizza", stack.pop(0))
        self.assertEqual("is", stack.pop(0))
        self.assertEqual("this", stack.pop(0))
        self.assertRaises(ValueError, stack.pop, 0)

        self.assertEqual(99, stack.pop(2))
        self.assertEqual(135678, stack.pop(2))
        self.assertRaises(ValueError, stack.pop, 2)

        self.assertItemsEqual([0, 0, 0], stack.entries)

    def test_multi_stack_four_stacks(self):
        """
        Checks the multi-stack model performs correctly with four stacks
        """
        stack = MultiStack(4)

        stack.push(3, (4, 5, 6))
        stack.push(0, "this")
        stack.push(2, "abc")
        stack.push(2, "def")
        stack.push(0, "is")
        stack.push(1, 135678)
        stack.push(1, 99)
        stack.push(0, "pizza")
        stack.push(0, "with")
        stack.push(0, "extra")
        stack.push(0, "cheese")
        stack.push(3, (7, 8, 9))

        self.assertEqual("def", stack.pop(2))
        self.assertEqual("abc", stack.pop(2))
        self.assertRaises(ValueError, stack.pop, 2)

        self.assertEqual("cheese", stack.pop(0))
        self.assertEqual("extra", stack.pop(0))
        self.assertEqual("with", stack.pop(0))
        self.assertEqual("pizza", stack.pop(0))
        self.assertEqual("is", stack.pop(0))
        self.assertEqual("this", stack.pop(0))
        self.assertRaises(ValueError, stack.pop, 0)

        self.assertEqual(99, stack.pop(1))
        self.assertEqual(135678, stack.pop(1))
        self.assertRaises(ValueError, stack.pop, 1)

        self.assertEqual((7, 8, 9), stack.pop(3))
        self.assertEqual((4, 5, 6), stack.pop(3))
        self.assertRaises(ValueError, stack.pop, 3)

        self.assertItemsEqual([0, 0, 0, 0], stack.entries)

    def test_min_stack(self):
        """
        Tests the stack correctly reports its minimum value
        """
        stack = MinStack()

        # Check adding values
        stack.push(3)
        self.assertEqual(3, stack.minimum)
        stack.push(5)
        self.assertEqual(3, stack.minimum)
        stack.push(1)
        self.assertEqual(1, stack.minimum)

        # Check removing values
        self.assertEqual(1, stack.pop())
        self.assertEqual(3, stack.minimum)
        self.assertEqual(5, stack.pop())
        self.assertEqual(3, stack.minimum)
        self.assertEqual(3, stack.pop())

        with self.assertRaises(ValueError):
            _ = stack.minimum
