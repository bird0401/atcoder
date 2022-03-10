n,m=map(int,input().split())
xy=[set(map(lambda t:int(t)-1, input().split())) for i in range(m)]
from itertools import *
ans=0
for i in range(2**n):
    mem=[]
    for j in range(n):
        if (i>>j)&1:mem+=[j]
        if all(set([x,y]) in xy for x,y in combinations(mem,2)):
            ans=max(ans,len(mem))
print(ans)
