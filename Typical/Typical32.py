n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
m=int(input())
xy=[[0]*n for _ in range(n)]
for i in range(m):
    x,y=map(int, input().split())
    xy[x-1][y-1]=1;xy[y-1][x-1]=1
inf=10**20;mint=inf
from itertools import *
for p in permutations(range(n)):
    t=0
    for i in range(n):
        if i<n-1 and xy[p[i]][p[i+1]]==1:t=inf;break
        t+=a[p[i]][i]
    mint=min(mint,t)
print(-1 if mint==inf else mint)