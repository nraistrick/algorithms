"""
Contains a selection of stack and queue related algorithms
"""


class MultiStack(object):
    """
    Maintains multiple stacks and store them simultaneously on a single,
    internal, shared list. It works under the following principles:

    * The first N entries represent a pointer to the top of each supported
    stack where we have N stacks in total
    * Several stacks share the same underlying data structure. A single stack
    entry is a group of three values which includes the value itself, the stack ID
    the entry belongs to and a pointer to the last previous entry in the same
    stack. The latter assists with updating a stack's pointer after a pop operation.

    Example:

    T = Pointer to top of each stack
    I = Unique stack ID that each entry belongs to
    P = Number of entries away from the previous entry in the stack
    V = Value

                         (stack entry)
                         <------------> <------------> <-----------> <----------> <---------->
    Index:   | 0   1  2 | 3  4  5      | 6  7  8      | 9  10 11    | 12 13 14   | 15 16  17  |
    Identity | T   T  T | I  P  V      | I  P  V      | I  P  V     | I  P  V    | I  P   V   |
    ---------+----------+--------------+--------------+-------------+------------+------------+----
    Entries: |[17, 0, 14, 0, 0, "hello", 0, 1, "world", 0, 1, "this", 2, 0, "abc", 0, 2, "is" ...]
    """
    EMPTY_STACK = 0        # The value of each stack pointer if it has no entries
    NO_PREVIOUS_ENTRY = 0  # The default value to point back to for the first stack entry
    ENTRY_SIZE = 3         # The standard size for a single stack entry

    def __init__(self, number_of_stacks):
        """
        :param int number_of_stacks: The number of stacks you want to maintain
        """
        self.number_of_stacks = number_of_stacks
        self.entries = [self.EMPTY_STACK for _ in range(number_of_stacks)]

    def push(self, stack_id, value):
        """
        Adds an entry to the top of the specified stack

        :param int stack_id: The unique, numeric stack identifier
        :param value: A value to push onto the stack
        """
        self._check_stack_id(stack_id)

        top_of_stack = self.entries[stack_id]
        if top_of_stack == self.EMPTY_STACK:
            distance_from_last_entry = self.NO_PREVIOUS_ENTRY
        else:
            distance_from_last_entry = ((len(self.entries) - top_of_stack)/self.ENTRY_SIZE) + 1

        self.entries.append(stack_id)
        self.entries.append(distance_from_last_entry)
        self.entries.append(value)

        # Update the stack-specific pointer to point to the new stack head
        self.entries[stack_id] = len(self.entries) - 1

    def pop(self, stack_id):
        """
        Removes and retrieves an entry from the top of the specified stack

        :param int stack_id: The unique, numeric stack identifier
        :return: The top stack value
        """
        self._check_stack_id(stack_id)

        top = self.entries[stack_id]
        if top == self.EMPTY_STACK:
            raise ValueError("No entries left on stack with ID %d" % stack_id)

        # Get and remove stack entry
        entry = self.entries.pop(top)
        previous = self.entries.pop(top - 1)
        assert self.entries.pop(top - 2) == stack_id

        # Update pointer to new top of stack
        if previous == self.NO_PREVIOUS_ENTRY:
            self.entries[stack_id] = self.EMPTY_STACK
        else:
            self.entries[stack_id] -= previous * self.ENTRY_SIZE

        self._update_other_stack_pointers(stack_id, top)

        return entry

    def _check_stack_id(self, stack_id):
        """
        Checks we have support for the specific stack ID

        :param int stack_id: The unique, numeric stack identifier
        """
        if stack_id >= self.number_of_stacks:
            raise ValueError("No support for a stack ID of %d" % stack_id)

    def _update_other_stack_pointers(self, stack_id, top):
        """
        Update pointers for entries in other stacks which have been
        affected by removal of an entry from the current stack.
        For every stack except the current, the first entry it holds that
        follows the removed entry must have its previous-entry pointer decreased
        by one.

        :param int stack_id: The ID of the stack which has had an element removed
        :param int top: The top of the specified stack prior to having an
        element removed
        """
        stack_seen = [False for _ in range(self.number_of_stacks)]
        stack_seen[stack_id] = True

        for i in range(0, len(self.entries[top - 2:]), self.ENTRY_SIZE):
            previous_pointer = i + top - 1
            recorded_stack_id = self.entries[previous_pointer - 1]

            # We only update the first following entry of any other stack
            if stack_seen[recorded_stack_id]:
                continue

            stack_seen[recorded_stack_id] = True
            self.entries[recorded_stack_id] -= self.ENTRY_SIZE
            if self.entries[previous_pointer] != self.NO_PREVIOUS_ENTRY:
                self.entries[previous_pointer] -= 1


class MinStack(object):
    """
    Represents a stack which in addition to push and pop, also has a method
    to retrieve the minimum value of all entries on the stack in O(1) time
    """
    class MinNode(object):
        """
        Represents a node in a singly linked-list that also holds
        the current minimum value of all entries in the list
        """
        def __init__(self, value, minimum=None, last=None):
            """
            :param int value: The value of the node
            :param int minimum: The minimum value of all nodes in the list
            :param MinNode last: The last node in the list
            """
            self.value = value
            self.minimum = minimum
            self.last = last

    def __init__(self):
        self.head = None  # type: MinStack.MinNode

    def push(self, value):
        """
        Pushes a new value onto the stack
        :param int value: The numeric value
        """
        if self.head is None:
            self.head = self.MinNode(value, value)
        else:
            self.head = self.MinNode(value, min(value, self.head.minimum), self.head)

    def pop(self):
        """
        Pops the top value from the stack
        :return: The top value on the stack
        :rtype int
        """
        top = self.head
        self.head = self.head.last
        return top.value

    @property
    def minimum(self):
        """
        :return: The smallest current value on the stack
        :rtype: int
        """
        if self.head is None:
            raise ValueError("No minimum value available. Stack is empty")
        return self.head.minimum
