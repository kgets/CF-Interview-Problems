'''
def firstDuplicate(a):
    c=set()
    for e in a:
        if e in c:
            return e
        else:
            c.add(e)
    return -1
'''
def firstDuplicate(a):
    for x in a:
        #print(x)
        a[abs(x) - 1] *= -1
        if a[abs(x) - 1] > 0:
            return abs(x)
        #print(A)
    return -1

## use negative (-) to mark the locations of numbers you have already seen.
## This allows O(1) space complexity.
## ~O(2n) ==> O(n)
