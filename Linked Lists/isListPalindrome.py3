# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def isListPalindrome(l):
    n=1
    point=midpoint=l
    
    #find midpoint
    while point and point.next:
        point=point.next
        n+=1
        if n>1:
            n=0
            midpoint=midpoint.next
    #if odd shift right
    if midpoint and n==1:
        midpoint=midpoint.next
    
    #reverse second half of list
    prevp=None
    point=midpoint
    while point and point.next:
        nextp=point.next
        point.next=prevp
        prevp=point
        point=nextp
    if point:
        point.next=prevp
    
    #check each 
    while point:
        if l.value!=point.value:
            return 0
        point=point.next
        l=l.next
    return 1
