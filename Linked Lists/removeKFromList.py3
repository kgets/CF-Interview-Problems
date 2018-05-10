# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def removeKFromList(l, k):
    st=l
    while st and st.value==k:
        st=st.next
    l=st
    while l and l.next:       
        if l.next.value==k:
            l.next=l.next.next
        else:
            l=l.next
    return st if st else []
