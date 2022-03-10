n,m=map(int,input().split())
s=[int(input()) for _ in range(n)]+[0]
sums=sorted(list(set(e1+e2 for e1 in s for e2 in s)))
from bisect import bisect
print(max(sums[bisect(sums,m-e)-1]+e for e in sums if e<=m))