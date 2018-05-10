def rotateImage(a):
    l=len(a)-1
    for y in range(l+2//2):
        for x in range(y,l-y):
            t,a[x][l-y]=a[x][l-y],a[y][x]
            t,a[l-y][l-x]=a[l-y][l-x],t
            t,a[l-x][y]=a[l-x][y],t
            a[y][x]=t
    return a
