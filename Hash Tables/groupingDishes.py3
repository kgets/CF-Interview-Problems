def groupingDishes(dishes):
    #create dict for key: ingredient and value: (set) dishes included in
    d=dict()
    for e in dishes:
        for ing in e[1:]:
            if ing in d:
                d[ing].add(e[0])
            else:
                d[ing] = {e[0]}
                
    #any ingredients in more than one dish are sorted into the return list
    l=[]
    for name, lis in d.items():
        if len(lis)>1:
            l+=[[name]+list(sorted(lis))]
    return sorted(l)
        
