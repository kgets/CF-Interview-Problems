#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def kthSmallestInBST(t, k):
    return DFSleftfirst(t,k)[0]

def DFSleftfirst(t,k):
    if t:
        if t.left and k>0:
            v,k=DFSleftfirst(t.left,k)
        if k>0:
            k-=1
            v,k=t.value,k
        if t.right and k>0:
            v,k=DFSleftfirst(t.right,k)
        return v,k
            
