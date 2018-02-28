#encoding=utf-8
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
        p1 = l1 # 保护原始参数链表头部
        p2 = l2
        carry = 0
        v1 = v2 = 0
        dummyHead = ListNode(0) # 哑变量
        curr = dummyHead # 保护返回结果链表头部

        while p1 != None or p2 != None:

            # 判断是否为空
            if p1 == None:
                v1 = 0
            else:
                v1 = p1.val
            if p2 == None:
                v2 = 0
            else:
                v2 = p2.val

            # 求和
            num = v1+v2+carry
            carry = num/10
            curr.next = ListNode(num%10)
            curr = curr.next

            # 向下继续
            if p1 != None:
                p1 = p1.next
            if p2 != None:
                p2 = p2.next
        if carry > 0:
            curr.next = ListNode(carry)
        return dummyHead.next

if __name__ == "__main__":

    o1 = ListNode(2)
    o2 = ListNode(4)
    o3 = ListNode(3)
    o1.next = o2
    o2.next = o3

    k1 = ListNode(5)
    k2 = ListNode(6)
    k3 = ListNode(4)
    k1.next = k2
    k2.next = k3

    s = Solution()
    ans = s.addTwoNumbers(o1,k1)

    p = ans
    while p != None:
        print p.val
        p = p.next




