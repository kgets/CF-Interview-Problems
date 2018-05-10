# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def rearrangeLastN(l, n):
    if n==0 or l==None:
        return l
    #keep start of list
    #keep list of nodes n long (endNodelist)
    #remove from start and add to end as you progress through l
    cp=l #list looping pointer
    stp=l #holds start of left list
    endp=l #holds end of left list
    se=l #holds start of right list
    ee=l #holds end of right list
    nll=0 #ensures len of right list is <=n
    while cp:
        if nll>=n:
            #shift list right
            endp=se
            se=se.next
            ee=cp
        else:
            #increase list size
            ee=cp
        nll+=1
        cp=cp.next
    print(stp.value, endp.value, se.value, ee.value)
    if nll>n:
        ee.next=stp
        endp.next=None
    else:
        return l
    return se
