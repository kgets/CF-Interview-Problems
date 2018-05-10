#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def deleteFromBST(t, queries):
    for e in queries:
        t=deleteNode(t,e)
        #printTree(t)
    return t

'''
def printTree(t):
    if t:
        print(t.value)
        if t.right and t.left:
            print('left')
            printTree(t.left)
            print('right')
            printTree(t.right)
        elif t.left:
            print('left')
            printTree(t.left)
        elif t.right:
            print('right')
            printTree(t.right)
'''          
def deleteNode(t,v):
    #returns new subtree
    if not t:
        return t
    if v==t.value:
        #handle removal
        #print("equal")
        if t.left:
            #print('has left')
            _=Tree(0)
            if not t.left.right:
                tv=t.left.value
                t.left=t.left.left
                t.value=tv
            else:
                t.value=findRightmostNode(_,t.left)
        elif t.right:
            t=t.right
        else:
            t=None
    elif v>t.value:
        #descend right
        #print("move right")
        t.right=deleteNode(t.right,v)
    else:
        #descend left
        #print("move left")
        t.left=deleteNode(t.left,v)
    return t

def findRightmostNode(root,t):
    #find rightmost node, set = null, return value
    if t.right:
        return findRightmostNode(t,t.right)
    else:
        if t.left:
            root.right=t.left
        else:
            root.right=None
        #print('nr:', t.value)
        return t.value
