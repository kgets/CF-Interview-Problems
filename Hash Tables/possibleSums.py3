def possibleSums(coins, quantity):
    rs=set([0])
    for i,e in enumerate(coins):
        q=1
        ts=set()
        #combo current coin
        while q<=quantity[i]:
            for ec in rs:
                ts.add(ec+e*q)
            q+=1
        rs=rs.union(ts)        
    return len(rs)-1
