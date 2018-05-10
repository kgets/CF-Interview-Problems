def findSubstrings(words, parts):
    #implement a TRIE
    # {a:none , m: {e: {l:none}}, l: {o: {n}}, ...} 
    d=dict() #TRIE
    for w in parts:
        d = insertTrie(d, w)
    #loop through words checking for pattern
    nw=[]
    for w in words:
        nw.append(findTriePattern(w,d))
    return nw      
            
def insertTrie(d, w):
    #creates TRIE tree (implementation is in interlayed dictionaries)
    if w:
        if w[0] in d:
            if w[1:]:
                insertTrie(d[w[0]], w[1:])
            else:
                d[w[0]]['~']='end'
        else:
            if w[1:]:
                d[w[0]]=dict()
            else:
                d[w[0]]={'~': 'end'}
            insertTrie(d[w[0]], w[1:])
    return d

def findTriePattern(w,cd):
    #take w and TRIE d
    #return w with [] around pattern
    mss = ''
    lw=w
    while lw:
        nss=triePath(lw, cd, [''])
        if nss:
            nss=sorted(nss, key=lambda x: len(x))[-1]
            if len(nss)>len(mss):
                mss=nss
        lw=lw[1:]
    mi=w.find(mss)
    if mss!='':
        return w[:mi]+'['+mss+']'+w[mi+len(mss):]
    else:
        return w

def triePath(w,cd, css):
    #take w,d
    #return valid substring list
    #print(w)
    #print(cd)
    if w:
        if '~' in cd:
            css.append(css[0])
        if w[0] in cd:
            cd=cd[w[0]]
            css[0]=css[0]+w[0]
            return triePath(w[1:], cd, css)
        else:
            return css[1:]
    else:
        if '~' in cd:
            return css
        else:
            return css[1:]
    
        
        
    
    
    
    
    
    '''
    ret=[]
    parts=sorted(parts, key=lambda x: len(x), reverse=True)
    for w in words:
        match=''
        matchl=0
        matchi=len(w)
        for substr in parts:
            l=len(substr)
            if l<matchl:
                break
            if substr in w:
                #print(substr,' in ',w)
                cMatchi=w.find(substr)
                if cMatchi<matchi:
                    matchi=cMatchi
                    matchl=l
                    match=w[:matchi]+'['+substr+']'+w[matchi+l:]
        if match=='':
            ret.append(w)
        else:
            ret.append(match)
    return ret
    '''
