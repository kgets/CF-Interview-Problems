def firstNotRepeatingCharacter(s):
    while s:
        m=s.split(s[0])
        if len(m)==2:
            return s[0]
        s=''.join(m)
    return '_'
