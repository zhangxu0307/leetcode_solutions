# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n1.next = n2
n2.next = n3
n3.next = n4



def swapPairs(head):
    dum = ListNode(0)
    dum.next = head
    curr = dum
    while curr.next and curr.next.next:
        tmp = curr.next.next
        curr.next.next = tmp.next
        tmp.next = curr.next
        curr.next = tmp
        curr = curr.next.next
    return dum.next

tmp = n1
while tmp != None:
    print tmp.val
    tmp = tmp.next

print '------'
newHead = swapPairs(n1)
tmp = newHead
while tmp != None:
    print tmp.val
    tmp = tmp.next







