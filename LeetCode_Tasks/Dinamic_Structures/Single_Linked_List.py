"""Creating single linked list functionality"""


class SingleLinkedList:
    """This class defines the functionality of a single linked list"""

    class SingleLinkNode:
        """Single node of the single linked list"""

        def __init__(self, value, next=None) -> None:
            """
            Initialize the node with a value and a pointer to the next node.

            Args:
            value: The value stored in this node.
            next: The reference to the next node in the list. Defaults to None.
            """
            self.value = value
            self.next = next

    def __init__(self) -> None:
        """Initialize an empty single linked list."""
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
        """Append a value to the end of the single linked list."""
        new_node = self.SingleLinkNode(
            value)  # Create a new node with the given value

        if self.head is None:  # If the list is empty
            self.head = new_node  # The new node becomes the head
            self.tail = new_node  # The new node also becomes the tail
        else:
            self.tail.next = new_node  # Link the current tail to the new node
            self.tail = new_node  # Update the tail to the new node

    def insert(self, value: int, index: int):
        """Insert a value at the specified index in the list."""
        if index < 0:
            raise IndexError("Index must be a non-negative integer.")

        if self.head is None:  # If the list is empty
            if index == 0:
                # Insert at the head if index is 0
                self.head = self.SingleLinkNode(value)
                self.tail = self.head  # Since it's the only node, it becomes the tail
            else:
                raise IndexError(
                    "List is empty, so the only valid index is 0.")
            return

        if index == 0:  # Insert at the head of the list
            new_node = self.SingleLinkNode(value, self.head)
            self.head = new_node
            return

        current = self.head
        counter = 0

        # Traverse the list to find the correct position
        while current:
            if counter == index - 1:
                new_node = self.SingleLinkNode(value, current.next)
                current.next = new_node

                if new_node.next is None:  # If inserting at the end, update the tail
                    self.tail = new_node
                return

            current = current.next
            counter += 1

        raise IndexError("Index out of bounds.")

    def delete_element(self, index: int):
        """Delete element with selected index"""
        if index < 0:
            raise IndexError("Index must be a non-negative integer.")

        if self.head is None:  # If the list is empty
            raise IndexError("The list is empty")

        if index == 0:  # Deleting the head
            self.head = self.head.next
            if self.head is None:  # If the list becomes empty after deletion
                self.tail = None  # Update tail to None
            return

        current = self.head
        counter = 0

        # Traverse the list to find the node just before the one to delete
        while current:
            if counter == index - 1:
                to_delete = current.next
                if to_delete is None:
                    raise IndexError("Index out of bounds.")

                current.next = to_delete.next

                if current.next is None:  # If the last node was deleted
                    self.tail = current  # Update the tail to the previous node
                return

            current = current.next
            counter += 1

        raise IndexError("Index out of bounds.")

    def merge_list_with_another(self, another_list):
        """Merges two sorted lists"""
        original_list = self.head
        second_list = another_list.head

        if original_list is None:  # If the original list is empty
            self.head = second_list  # Just point to the second list
            self.tail = another_list.tail
            return

        if second_list is None:  # If the second list is empty
            return

        # Dummy node to help build the merged list
        dummy = self.SingleLinkNode(0)
        new_list_tail = dummy

        # Merge the two lists by comparing values
        while original_list and second_list:
            if original_list.value <= second_list.value:
                new_list_tail.next = original_list
                original_list = original_list.next
            else:
                new_list_tail.next = second_list
                second_list = second_list.next
            new_list_tail = new_list_tail.next

        # If one list is exhausted, append the remaining elements of the other list
        new_list_tail.next = original_list if original_list else second_list

        self.head = dummy.next  # The head of the merged list

        # Update the tail to the last node of the merged list
        while new_list_tail.next:
            new_list_tail = new_list_tail.next

        self.tail = new_list_tail

    def sort_list(self, order: bool = False):
        """Sort the list in ascending or descending order."""
        if self.head is None:
            return

        # Extract values from the linked list
        current = self.head
        values = []
        while current:
            values.append(current.value)  # Add each node's value to the list
            current = current.next

        # Sort the list in the desired order
        # `order` determines ascending or descending
        values.sort(reverse=order)

        # Rebuild the linked list with sorted values
        current = self.head
        for value in values:
            current.value = value  # Update node's value with the sorted value
            current = current.next

        # No need to update self.tail since structure of linked list remains the same

    def __getitem__(self, index: int):
        """Overload the square brackets for getting a value by index."""
        if index < 0:
            raise IndexError("Index must be a non-negative integer.")

        current = self.head
        counter = 0

        while current:
            if counter == index:
                return current.value
            current = current.next
            counter += 1

        raise IndexError("Index out of bounds.")

    def __setitem__(self, index: int, value):
        """Overload the square brackets for setting a value by index."""
        if index < 0:
            raise IndexError("Index must be a non-negative integer.")

        current = self.head
        counter = 0

        while current:
            if counter == index:
                current.value = value
                return
            current = current.next
            counter += 1

        raise IndexError("Index out of bounds.")

    def __len__(self):
        """Return the length of the list."""
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def __str__(self):
        """Return a string representation of the list."""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.value))
            current = current.next
        return " -> ".join(elements) + " -> None"
