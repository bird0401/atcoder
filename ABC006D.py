n=int(input())
c=[int(input()) for _ in range(n)]

from bisect import bisect_left
l,cnt=[],0
for e in c:
    m=bisect_left(l,e)
    if m==len(l):l+=[e]
    else:
        l[m]=e
        cnt+=1
print(cnt)