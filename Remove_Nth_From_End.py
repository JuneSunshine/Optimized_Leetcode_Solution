class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self is None:
            return "Nil"
        else:
            return "{} -> {}".format(self.val, repr(self.next))

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # dummy = ListNode(-1)
        # # print (dummy)
        # dummy.next = head
        # slow, fast = dummy, dummy
        # print (slow,fast)
        #
        # for i in range(n):
        #     fast = fast.next
        #     print (fast)
        #
        # while fast.next:
        #     slow, fast = slow.next, fast.next
        #
        # slow.next = slow.next.next
        #
        # return dummy.next

        firstpointer = head
        secondpointer = head
        for i in range(n):

            if firstpointer.next != None:
                firstpointer = firstpointer.next
            else:
                head = head.next
                return head

        while firstpointer.next != None:
            firstpointer = firstpointer.next
            secondpointer = secondpointer.next
        secondpointer.next = secondpointer.next.next

        return head


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    print (Solution().removeNthFromEnd(head, 2))
