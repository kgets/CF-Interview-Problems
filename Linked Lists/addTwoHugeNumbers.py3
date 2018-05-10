# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
def addTwoHugeNumbers(a, b):
    #dont know how many elements are in the list node until we .next through the list.
    #should reverse the lists then add
    a=revListNode(a)
    b=revListNode(b)
    co=0 #carry over
    pnode=None
    while a or b or co:
        if a and b:
            n=a.value+b.value+co
            a=a.next
            b=b.next
        elif a:
            n=a.value+co
            a=a.next
        elif b:
            n=b.value+co
            b=b.next
        else:
            n=co
        cnode=ListNode(n%1e4)
        cnode.next=pnode
        co=n//1e4        
        pnode=cnode
    return pnode
            


def revListNode(ln):
    pn=None
    while ln:
        nn=ln.next
        ln.next=pn
        pn=ln
        ln=nn
    return pn
        
