def autocomplete(wordList,actions):
    #crete tree
    t=Trie(None,wordList)
    t.createTree()
    s=''
    ACL=[]
    for e in actions:
        if e == "PAUSE":
            ACL.append(list(t.findNode(s)))
        elif e == "BACKSPACE":
            s=s[:-1]
        else:
            s+=e
    return ACL
            
class Trie:
    def __init__(self,letter,wordList):
        self.letter=letter # letter in trie
        self.validWords=wordList #valid words
        self.children=dict() # { Child Letter: child node }
    def createTree(self):
        for w in self.validWords:
            self.createBranch(w,w)   
    def createBranch(self,w,fw):
        if w[0] not in self.children:
            self.children[w[0]]=Trie(w[0],set())
        nextNode=self.children[w[0]]
        nextNode.validWords.add(fw)
        if len(w)>1:
            nextNode.createBranch(w[1:],fw)
    def findNode(self,string):
        if string and string[0] in self.children:
            return self.children[string[0]].findNode(string[1:])
        elif string:
            return []
        else:
            return sorted(self.validWords)
            
            
'''
def autocomplete(wordList, actions):
    wordList=sorted(wordList)
    ACL=[]
    s=''
    for e in actions:
        if e == "PAUSE":
            ACL.append(validWord(s,wordList))
        elif e == "BACKSPACE":
            s=s[:-1]
        else:
            s+=e
    return ACL

def validWord(s,wordList):
    wl=[]
    for e in wordList:
        if e.startswith(s):
            wl.append(e)
    return wl
'''
