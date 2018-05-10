#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def isTreeSymmetric(t):
    tr=t
    # carry out a symmetric DFS  
    return checkSym(t,tr)

def checkSym(lb,rb):
    if lb and rb:
        if lb.value != rb.value:
            return 0
        if lb.left and rb.right and lb.right and rb.left:
            return checkSym(lb.left, rb.right) and checkSym(lb.right,rb.left)
        elif lb.left and rb.right:
            return checkSym(lb.left, rb.right)
        elif lb.right and rb.left:
            return checkSym(lb.right,rb.left)
        elif not lb.right and not lb.left and not rb.right and not rb.left:
            return 1
        else:
            return 0
    elif lb or rb:
        return 0
    else:
        return 1
        
