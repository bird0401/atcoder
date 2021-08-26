from sys import stdin
from collections import Counter

n,k=[int(x) for x in stdin.readline().rstrip().split()]
st=list(stdin.readline().rstrip())
stsor=sorted(st)
ans=""
d=0
counter=Counter(st[:1])
for i in range(len(st)):
    for C in stsor:
        d1=d+(C!=st[i])
        d2=sum(counter.values())-(counter[C]>0) 
        if d1+d2<=k:
            ans+=C
            stsor.remove(C)
            d=d1
            counter=Counter(st[:i+2])-Counter(ans)
            break
print(ans)