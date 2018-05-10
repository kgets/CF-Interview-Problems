def findProfession(level, pos):
    level-=1
    xor=3
    shift=2
    n=2
    while level:
        n = (n << shift) + (n ^ xor)
        xor = (xor << shift) + xor
        shift*=2
        level-=1
    return 'Engineer' if (1&(n>>(shift-pos))) else 'Doctor'
