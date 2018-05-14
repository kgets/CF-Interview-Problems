def climbingStairs(n):
    fib=[1,1]
    while n:
        fib[0],fib[1]=fib[1],fib[0]+fib[1]
        n-=1
    return fib[0]
