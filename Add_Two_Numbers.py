'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # idea add l2 to l1
        original_head = l1
        carry = 0

        while l2 is not None:
            # for this step
            val = l1.val + l2.val + carry
            carry = 0

            if val >= 10:
                val = val - 10
                carry = 1

            l1.val = val

            # for next step
            # prepare l2
            l2 = l2.next

            # prepare l1
            if l2 is not None and l1.next is None:
                l1.next = ListNode(0)

            if l2 is not None:
                l1 = l1.next

        while carry == 1:
            # prepare l1
            if l1.next is None:
                l1.next = ListNode(1)
                break

            l1 = l1.next

            val = l1.val + carry
            carry = 0

            if val >= 10:
                val = val - 10
                carry = 1

            l1.val = val

        return original_head

