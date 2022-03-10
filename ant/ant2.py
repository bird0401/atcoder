n=int(input())
xy=[list(map(int, input().split())) for i in range(n)]
ans=0
for i in range(n):
    x1,y1=xy[i]
    for j in range(n):
        x2,y2=xy[j]
        ans=max(ans,(x1-x2)**2+(y1-y2)**2)
from math import *
print(sqrt(ans))