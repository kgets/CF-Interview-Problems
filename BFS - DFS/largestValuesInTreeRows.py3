#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def largestValuesInTreeRows(t):
    if not t:
        return []
    al=[]
    l=[t]
    while l:
        nl=[]
        cvl=[]
        for e in l:
            cvl.append(e.value)
            if e.left is not None:
                nl.append(e.left)
            if e.right is not None:
                nl.append(e.right)
        l=nl
        al.append(max(cvl))
    return al
