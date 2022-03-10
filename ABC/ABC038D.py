n=int(input())
wh=[list(map(int,input().split())) for i in range(n)]
wh.sort(key=lambda t:(t[0],-t[1]))
from bisect import *
LIS=[wh[0][1]]
for i in range(1,n):
    w,h=wh[i]
    if h>LIS[-1]:
        LIS.append(h)
    else:LIS[bisect_left(LIS, h)]=h
print(len(LIS))
