#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
'''
def restoreBinaryTree(inorder, preorder):
    PO_0=preorder.pop(0) #preorder naught
    IO_0=inorder.pop(0)  #inorder naught
    t=Tree(PO_0)         #tree bottom root
    root=t               #pointer to current root
    leftStack=dict()     #stack left of current root :: d[value_IO] = index_entry_queue
    while PO_0:
        if IO_0==PO_0:
            LBP=root #left branch pointer
            while PO_0 in leftStack:
                
            #set root
            #Create left tree
            #next PO_0 is right branch
            PO_0=preorder.pop(0)
            root.right=Tree(PO_0)
                
        else:
            leftStack.append(IO_0)
            IO_0=inorder.pop(0)

    return t
'''
def restoreBinaryTree(inorder, preorder):
    return tInit(inorder,preorder)
    
def leftSubTree(t,inorder,preorder):
    #print('Left Branch')
    t=Tree(preorder.pop(0))
    iLeft=inorder.pop(0)
    Left=[]
    #find all left branches
    while iLeft!=t.value:
        Left.append(iLeft)
        iLeft=inorder.pop(0)
    Right=preorder[:len(Left)]
    preorder=preorder[len(Left):]
    #print('CR:',t.value)
    #print('LR:',Left,Right)
    #print('IP:',inorder,preorder)
    if Left:
        t.left=leftSubTree(t,Left,Right)
    if preorder:
        t.right=rightSubTree(t,inorder,preorder)
    return t
        
def rightSubTree(t,inorder,preorder):
    #print("Right Branch")
    t=Tree(preorder.pop(0))
    iLeft=inorder.pop(0)
    Left=[]
    #find all left branches
    while iLeft!=t.value:
        Left.append(iLeft)
        iLeft=inorder.pop(0)
    Right=preorder[:len(Left)]
    preorder=preorder[len(Left):]
    #print('CR:',t.value)
    #print('LR:',Left,Right)
    #print('IP:',inorder,preorder)
    if Left:
        t.left=leftSubTree(t,Left,Right)
    if preorder:
        t.right=rightSubTree(t,inorder,preorder)  
    return t

def tInit(inorder,preorder):
    #print("create tree")
    t=Tree(preorder.pop(0))
    iLeft=inorder.pop(0)
    Left=[]
    #find all left branches
    while iLeft!=t.value:
        Left.append(iLeft)
        iLeft=inorder.pop(0)
    Right=preorder[:len(Left)]
    preorder=preorder[len(Left):]
    #print('CR:',t.value)
    #print('LR:',Left,Right)
    #print('IP:',inorder,preorder)
    if Left:
        t.left=leftSubTree(t,Left,Right)
    if preorder:
        t.right=rightSubTree(t,inorder,preorder)
    return t
    
            
