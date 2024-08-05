"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. 
The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.
"""

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1: ListNode, list2: ListNode):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = ListNode()
        list3 = head

        if list1.val == list2.val:
            list3.next = list1
            list1 = list1.next
            list3 = list3.next
        elif list1.val > list2.val:
            list3.next = list1
            list1 = list1.next
            list3 = list3.next
        else:
            list3.next = list2
            list2 = list2.next
            list3 = list3.next

        return head.next
