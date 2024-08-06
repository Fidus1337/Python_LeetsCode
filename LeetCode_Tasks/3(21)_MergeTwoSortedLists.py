"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. 
The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """Function for merging two single-linked sorted lists"""
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next

    def print_result(self, list_input):
        """Function for printing all elements of single_linked list"""
        while list_input:
            print(f'{list_input.val} ', end='')
            list_input = list_input.next
        print()


# Example
first_list = ListNode(0, ListNode(1, ListNode(2, ListNode(10, None))))
second_list = ListNode(0, ListNode(1, ListNode(9, ListNode(8, None))))

sol = Solution()
merged_list = sol.mergeTwoLists(first_list, second_list)
sol.print_result(merged_list)
