import copy
import gc
def sumSubsets(arr, num):
    NL=sumNodeList(num)
    for e in arr:
        NL.addNode(e)   
    return NL.returnPaths()

class sumNodeList:
    def __init__(self,lim):
        #  dir    pathval, paths
        self.dir = { 0:   set('0') }
        self.lim = lim
    def addNode(self,value):
        ldir=copy.deepcopy(self.dir)
        for k,v in ldir.items():
            if k+value<=self.lim:
                #add key and path strings to dir
                if k+value in self.dir:
                    for ev in v:
                        self.dir[k+value].add(ev+','+str(value))
                else:
                    #create new
                    nv=set()
                    for ev in v:
                        nv.add(ev+','+str(value))
                    self.dir[k+value] = nv
            else:
                if k!=self.lim:
                    del self.dir[k]
        gc.collect()
                
    def returnPaths(self):
        paths=[]
        for e in self.dir[self.lim]:
            tL=[]
            e=e.split(',')[1:]
            for c in e:
                tL.append(int(c))
            paths.append(tL)
        return sorted(paths)
