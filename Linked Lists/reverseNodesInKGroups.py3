# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def reverseNodesInKGroups(l, k):
    rem=l
    pn=ListNode(-1)
    snode=pn
    while rem:
        pn.next,rem,pn=revListNode(rem,k)
    return snode.next
    

def revListNode(cpoint,k):
    pn=None
    stp=cpoint
    cnt=cpoint
    ck=k
    while cnt and ck:
        cnt=cnt.next
        ck-=1
    if ck>0:
        return stp,None,None
    while cpoint and k:
        nn=cpoint.next
        cpoint.next=pn
        pn=cpoint
        cpoint=nn
        k-=1
    stp.next=cpoint
    #returning (pn: starting node for rev list),(cpoint: pointer for remaining list to rev)
    #(stp: ending node for rev list)
    return pn,cpoint,stp
