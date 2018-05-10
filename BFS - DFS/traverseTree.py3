#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def traverseTree(t):
    if not t:
        return []
    al=[]
    l=[t]
    while l:
        nl=[]
        for e in l:
            al.append(e.value)
            if e.left is not None:
                nl.append(e.left)
            if e.right is not None:
                nl.append(e.right)
        l=nl
    return al
