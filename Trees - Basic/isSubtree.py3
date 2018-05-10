#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def isSubtree(t1, t2):
    if not t2:
        return 1
    elif t1 and t2:
        return treeIter(t1,t2)
    else:
        return 0
    
def isMatch(t1,t2):
    if t1 and t2:
        #print('\t',t1.value,t2.value)
        if t1.value!=t2.value:
            return 0
        if t1.left and t2.left and t1.right and t2.right:
            return isMatch(t1.left,t2.left) and isMatch(t1.right,t2.right)
        elif t1.left and t2.left:
            return isMatch(t1.left,t2.left)
        elif t1.right and t2.right:
            return isMatch(t1.right,t2.right)
        elif t1.left or t1.right or t2.left or t2.right:
            return 0
        else:
            return t1.value==t2.value
    elif not t1 and not t2:
        return 1
    else:
        return 0
        
def treeIter(t1,t2):
    #print('value match:',t1.value,t2.value)
    if t1.value==t2.value:
        #print(':matching:')
        if isMatch(t1,t2):
            return 1
    if t1.left and t1.right:
        #print('t1: left and right')
        return treeIter(t1.left,t2) or treeIter(t1.right,t2)
    elif t1.left:
        #print('t1: left')
        return treeIter(t1.left,t2)
    elif t1.right:
        #print('t1: right')
        return treeIter(t1.right,t2)
    else:
        return 0
