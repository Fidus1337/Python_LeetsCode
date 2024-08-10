"""Creating single linked list functionality"""


class SingleLinkNode:
    """SingleLinkNode definition (one piece of the single linked list)"""

    def __init__(self, value, next=None) -> None:
        """
        Initialize the node with a value and a pointer to the next node.

        Args:
            value: The value stored in this node.
            next: The reference to the next node in the list. Defaults to None.
        """
        self.value = value
        self.next = next


class SingleLinkedList:
    """This class defines the functionality of a single linked list"""

    def __init__(self) -> None:
        """
        Initialize an empty single linked list.
        """
        self.head = None  # Pointer to the first node in the list
        self.tail = None  # Pointer to the last node in the list

    def print_all_values(self):
        """Prints all values in the single linked list."""
        if self.head is None:
            print("No values in the list. Please, add new values to it.")
        else:
            current = self.head  # Temporary pointer to traverse the list
            while current:
                print(current.value, end=" -> ")
                current = current.next
            print("None")  # Indicates the end of the list

    def append(self, value: int):
        """
        Append a value to the end of the single linked list.

        Args:
            value: The value to append to the list.
        """
        new_node = SingleLinkNode(
            value)  # Create a new node with the given value

        if self.head is None:  # If the list is empty
            # The new node becomes both the head and the tail
            self.head = new_node
            self.tail = new_node
        else:
            # Link the current tail to the new node
            self.tail.next = new_node
            # Update the tail to be the new node
            self.tail = new_node

    def insert(self, value: int, index: int):
        """
        Insert a value at the specified index in the list.

        Args:
            value: The value to insert into the list.
            index: The position at which to insert the value. Indexing starts at 0.

        Raises:
            IndexError: If the index is out of the bounds of the list or is negative.
        """
        if index < 0:
            raise IndexError("Index must be a non-negative integer.")

        if self.head is None:  # If the list is empty
            if index == 0:
                # Insert the new node at the head
                self.head = SingleLinkNode(value)
                # Since it's the only node, update the tail as well
                self.tail = self.head
            else:
                raise IndexError(
                    "List is empty, so the only valid index is 0."
                )
            return

        if index == 0:  # Insert at the head of the list
            new_node = SingleLinkNode(value, self.head)
            self.head = new_node
            return

        current = self.head
        counter = 0

        # Traverse the list to find the correct position
        while current:
            if counter == index - 1:
                # Insert the new node at the desired index
                new_node = SingleLinkNode(value, current.next)
                current.next = new_node

                # If inserting at the end, update the tail
                if new_node.next is None:
                    self.tail = new_node
                return

            current = current.next
            counter += 1

        # If the index is beyond the end of the list
        raise IndexError("Index out of bounds.")

    def delete_element(self, index: int):
        """Delete element with selected index"""

        # The case when we have negative index
        if index < 0:
            raise IndexError("Index must be a non-negative integer.")

        # User cannot delete element from empty list
        if self.head is None:
            raise IndexError("The list is empty")

        # If we need to delete 0 index element
        if index == 0:
            self.head = self.head.next
            if self.head is None:
                return
            if self.head.next is None:
                self.tail = self.head
            return

        current = self.head
        counter = 0
        while current:
            if counter == index - 1:
                element_after_deleted = (current.next).next

                if element_after_deleted is None:
                    self.tail = element_after_deleted
                    current.next = element_after_deleted
                    return

                if element_after_deleted is not None:
                    current.next = element_after_deleted
                    return
                else:
                    self.head = current
                    self.tail = current
                    return


            # Testing the SingleLinkedList
test = SingleLinkedList()
test.append(5)
test.append(10)
test.print_all_values()

test.delete_element(0)
test.delete_element(0)
test.append(7)
test.delete_element(0)
test.print_all_values()
