def longestPath(fileSystem):
    fs=fileSystem.replace('    ','\t')
    fs=fs.split('\f')
    # count \t at start and create tuple with (3,'\t\t\tstring),(2,\t\tstring\t),..
    tfs=[]
    for e in fs:
        c=e.count('\t')
        while not e.startswith('\t'*c):
            c-=1
        tfs.append((c,e[c:]))
    #print(tfs)    
    #fill FileTree with fileSystem
    ft=FileTree('~root')
    ftp=ft #pointer
    plvl=-1 #prev level
    for e in tfs:
        if e[0]==plvl+1:
            ftp.children.append(FileTree(e[1]))
            ftp=ftp.children[-1]
            plvl+=1
        else:
            ftp=ft
            plvl=-1
            while e[0]!=plvl+1:
                ftp=ftp.children[-1]
                plvl+=1
            ftp.children.append(FileTree(e[1]))
            ftp=ftp.children[-1]
            plvl+=1
    
    #printFT(ft,0)
    return max(maxLenPathFT(ft,0,0)-7,0)
            
class FileTree:
    def __init__(self,value):
        self.value=value
        self.children=[]

def maxLenPathFT(ft,maxL,pathL):
    pathL += len(ft.value)+1
    if ft.value.count('.')>0:
        if pathL > maxL:
            maxL = pathL
        return maxL
    else:
        for e in ft.children:
            maxL = maxLenPathFT(e,maxL,pathL)
        return maxL
    
'''
def printFT(ft,lvl):
    print('\t'*lvl,ft.value)
    for e in ft.children:
        printFT(e,lvl+1)
'''
