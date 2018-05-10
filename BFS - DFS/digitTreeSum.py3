#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def digitTreeSum(t):
    ##I could just keep a sum and += when i reach a root, but that is no fun.
    arr=[]
    DFSroots(0, t, arr)
    print(arr)
    return sum(arr)
    
def DFSroots(val, t, arr):
    if t.left is None and t.right is None:
        arr.append(val*10+t.value)
        return 1
    elif t.left is None:
        return DFSroots(val*10+t.value, t.right, arr)
    elif t.right is None:
        return DFSroots(val*10+t.value, t.left, arr)
    else:
        return DFSroots(val*10+t.value, t.left, arr),DFSroots(val*10+t.value, t.right, arr)
