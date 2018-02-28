
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

n0 = ListNode(0)
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)

n0.next = n1
n1.next = n2
n2.next = n3
#n3.next = n2


def hasCycle(head):
    pfast = head
    pslow = head
    if pfast == None:
        return False
    while pfast != None and pfast.next != None:
        pfast = pfast.next.next
        pslow = pslow.next
        if pfast == pslow:
            return True
    return False

ans = hasCycle(n0)
print ans

