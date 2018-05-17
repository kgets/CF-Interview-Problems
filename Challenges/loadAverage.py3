import datetime as q
z=q.datetime.strptime

a=0.92004
b=0.98347
g=0.99446
f="%H:%M:%S"
h=' {:.2f}'
n='\n'

with open('proc.log', 'r') as _:
    c=_.read().split('\n')
    c=c[1:-1]
with open('system.log','r') as _:
    d=_.read().split('\n')
    t=z(d[0],f)
    r=z(d[1],f)

w=x=y=0
while t<r:
    N=0
    for e in c:
        _,j,k=e.split('|')
        p=z(j, f)
        if p<=t:
            N+= 1 if k=='START' else -1
    w=a*w+(1-a)*N
    x=b*x+(1-b)*N
    y=g*y+(1-g)*N
    print(('{:'+f+'}'+h*3).format(t,w,x,y))
    t+=q.timedelta(0,5)
