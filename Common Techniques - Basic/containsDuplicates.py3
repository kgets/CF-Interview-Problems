def containsDuplicates(a):
    s=set()
    for n in a:
        sl=len(s)
        s.add(n)
        if sl==len(s):
            return 1
    return 1
