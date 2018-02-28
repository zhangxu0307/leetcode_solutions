# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p = head
        index = 0
        while p != None:
            index += 1
            print index, p.val
            p = p.next
        length = index
        if n > length:
            return None
        index = 0
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        while p!= None:
            index += 1
            if index == length-n+1:
                p.next = p.next.next
                return dummy.next
            else:
                p = p.next

    def removeNthFromEnd2(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        for i in range(1,n+2):
            first = first.next
        while first != None:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next




head = ListNode(3)
node2 = ListNode(4)
node3 = ListNode(5)
node4 = ListNode(7)
head.next = node2
node2.next = node3
node3.next = node4
n = 2
s = Solution()
ans = s.removeNthFromEnd2(head,n)
while ans != None:
    print ans.val
    ans = ans.next
