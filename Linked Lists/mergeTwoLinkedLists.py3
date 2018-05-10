# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def mergeTwoLinkedLists(l1, l2):
    pnode=ListNode(-1)
    stp=pnode
    while l1 or l2:
        if l1 and l2:
            if l1.value>l2.value:
                cnode=ListNode(l2.value)
                l2=l2.next
            else:
                cnode=ListNode(l1.value)
                l1=l1.next
        elif l1:
            cnode=ListNode(l1.value)
            l1=l1.next
        else:
            cnode=ListNode(l2.value)
            l2=l2.next
        pnode.next=cnode
        pnode=cnode
    return stp.next
        
