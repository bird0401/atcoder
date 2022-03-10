n=int(input())
a=list(map(int, input().split()))
q=int(input())
b=[int(input()) for _ in range(q)]
a.sort()
from bisect import bisect_left
for sco in b:
    i=bisect_left(a,sco)
    if i==0:print(a[0]-sco)
    elif i==n:print(sco-a[n-1])
    else:print(min(a[i]-sco,sco-a[i-1]))