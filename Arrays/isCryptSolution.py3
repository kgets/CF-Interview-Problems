def isCryptSolution(crypt, solution):
    k = iter(solution)
    b = dict(k)
    for i,w in enumerate(crypt):
        s=''
        for c in w:
            s+=b[c]
        if s[0]=='0' and len(s)>1:
            return 0
        crypt[i]=int(s)
    return crypt[0]+crypt[1]==crypt[2]
