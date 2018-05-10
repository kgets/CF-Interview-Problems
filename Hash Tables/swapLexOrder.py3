import operator
def swapLexOrder(st, pairs):
    sd=dict()
    #create string dict
    for i,c in enumerate(st):
        sd[i]=c
    d=dict()
    #dictionary of connections
    for e in pairs:
        j,k=e[0],e[1]
        if j in d.keys():
            d[j].add(k)
        else:
            d[j]={j,k}
        if e[1] in d.keys():
            d[k].add(j)
        else:
            d[k]={j,k}
    #solve for combo sets
    cd=list() #combos list
    m=0
    while d:
        if m==0:
            ck,cv=d.popitem()
        m=0
        ncv=set()
        for ek in cv:
            if ek in d.keys():
                ncv=ncv.union(d[ek])
                del d[ek]
                m+=1
        cv=cv.union(ncv)
        if m==0 or not d:
            cd.append(cv)
        '''
        for ek,ev in d.items():
            if ck in ev:
                d[ek]=ev.union(cv)
                m+=1
        if m==0:
            cd.append(cv)
        '''
    #for each combo sort chars at index
    for e in cd:
        subdir=dict()
        for i in e:
            subdir[i-1]=sd[i-1]
        sortdir = sorted(subdir.items(), key=operator.itemgetter(1), reverse=True)
        for i in sorted(e):
            sd[i-1]=sortdir.pop(0)[1]
    return ''.join(sd.values())
