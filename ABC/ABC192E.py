from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20
from math import ceil

n,m,x,y=map(int,input().split())
graph=[[] for _ in range(n)]
for i in range(m):
    a,b,t,k=map(int,input().split())
    a-=1
    b-=1
    graph[a].append((b,t,k))
    graph[b].append((a,t,k))

from heapq import heappop,heappush
def dijk(st):
    seen=[False]*n
    dist=[inf]*n
    dist[st]=0
    hq=[(dist[st],st)]
    while hq:
        v=heappop(hq)[1]
        if seen[v]==True:
            continue
        seen[v]=True
        for to,cost,k in graph[v]:
            gcost=ceil(dist[v]/k)*k+cost
            if gcost<dist[to]:
                dist[to]=gcost
                heappush(hq,(gcost,to))
    return dist
xycost=int(dijk(x-1)[y-1])
print(-1 if xycost==inf else xycost)
