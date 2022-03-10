
k,n,m=map(int,input().split())
a=list(map(int, input().split()))
from math import floor,ceil
def f(x):
    l=[max(0,ceil(float(m*e-x)/n)) for e in a]
    r=[(m*e+x)//n for e in a]
    return sum(l)<=m<=sum(r)

def ansc(x):
    b=[max(0,ceil(float(m*e-x)/n)) for e in a]
    r=[(m*e+x)//n for e in a]
    sumb=sum(b)
    for i in range(k):
        x=min(m-sumb,r[i]-b[i])
        b[i]+=x
        sumb+=x
    return b

inf=10**20
l,r=-1,inf
while r-l>1:
    mid=(r+l)//2
    if f(mid):r=mid
    else:l=mid
print(*ansc(r))