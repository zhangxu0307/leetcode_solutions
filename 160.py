# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
            return None
        len1 = len2 = 0
        p1 = headA
        p2 = headB
        while p1:
            len1 += 1
            p1 = p1.next
        while p2:
            len2 += 1
            p2 = p2.next
        print(len1, len2)
        p1 = headA
        p2 = headB
        if len1 > len2:
            diff = len1-len2
            for i in range(diff):
                p1 = p1.next
            while p1 != p2:
                p1 = p1.next
                p2 = p2.next
        else:
            diff = len2-len1
            for i in range(diff):
                p2= p2.next
            while p1 != p2:
                p1 = p1.next
                p2 = p2.next
        if p1 != p2:
            return None
        else:
            return p1

s = Solution()

p1 = ListNode(1)
p2 = ListNode(2)
p3 = ListNode(3)
p4 = ListNode(4)
p5 = ListNode(5)
p6 = ListNode(6)

p1.next = p2
p2.next = p3
p4.next = p5
p5.next = p6

ans = s.getIntersectionNode(p1, p4)
print(ans)



