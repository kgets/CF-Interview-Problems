from pathlib import Path as z
p=z("/root/devops")
s=[]

    
def y(k,s):
    for e in k.iterdir():
        if e.is_symlink():
            s+=[[e,e.resolve()]]
        else:
            if e.is_dir():
                y(e,s)

y(p,s)
for e in sorted(s , key=lambda p: (p[0].parent,p[0])):
    print(e[0],e[1])
