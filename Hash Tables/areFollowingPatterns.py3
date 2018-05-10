def areFollowingPatterns(strings, patterns):
    d=dict() #key=pattern, value=string
    ps=set()
    for i in range(len(strings)):
        if strings[i] in ps:
            if patterns[i] not in d.keys() or d[patterns[i]]!=strings[i]:
                return 0                
        else:
            if patterns[i] in d.keys():
                return 0
            else:
                d[patterns[i]]=strings[i]
                ps.add(strings[i])        
    return 1
