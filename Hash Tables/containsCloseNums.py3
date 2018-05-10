def containsCloseNums(nums, k):
    d=dict() # number=key, last index location = definition
    for i,e in enumerate(nums):
        if e in d.keys():
            if i-d[e]<=k:
                return 1
        d[e]=i
    return 0
        
