# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        lstart = ListNode(0)
        lstart.next = ListNode(0)
        l = lstart
        sub = 0
        while True:
            if l1 != None and l2 != None:
                l = l.next
                l.val = (l1.val + l2.val + sub) % 10
                if l1.val + l2.val + sub >= 10:
                    sub = 1
                else:
                    sub = 0
                l.next = ListNode(0)
                l1 = l1.next
                l2 = l2.next
            if l1 == None and l2 != None:
                l = l.next
                l.val = (l2.val + sub) % 10
                if l2.val + sub >= 10:
                    sub = 1
                else:
                    sub = 0
                l.next = ListNode(0)
                l2 = l2.next
            if l1 != None and l2 == None:
                l = l.next
                l.val = (l1.val + sub) % 10
                if l1.val + sub >= 10:
                    sub = 1
                else:
                    sub = 0
                l.next = ListNode(0)
                l1 = l1.next
            if l1 == None and l2 == None:
                if sub == 1:
                    l = l.next
                    l.val = sub
                    l.next = None
                else:
                    l.next = None
                return lstart.next

if __name__ == '__main__':
    l1 = ListNode(3)
    l1.next = ListNode(7)
    l2 = ListNode(9)
    l2.next = ListNode(2)
    s = Solution().addTwoNumbers(l1,l2)
    print(s)