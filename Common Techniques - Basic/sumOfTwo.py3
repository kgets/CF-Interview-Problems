def sumOfTwo(a, b, v):
    s=set(a)
    return any(v-n in s for n in b)
