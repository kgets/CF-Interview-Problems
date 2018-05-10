#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def hasPathWithGivenSum(t, s):
    return DFSroots(0, t, s)
    
def DFSroots(csum, t, sval):
    if t:
        if t.left is None and t.right is None:
            return csum+t.value==sval
        elif t.left is None:
            return DFSroots(csum+t.value, t.right, sval)
        elif t.right is None:
            return DFSroots(csum+t.value, t.left, sval)
        else:
            return DFSroots(csum+t.value, t.left, sval) or DFSroots(csum+t.value, t.right, sval)
    else:
        return csum==sval
