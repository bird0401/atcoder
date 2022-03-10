from sys import stdin
from heapq import heappop,heappush,heapify

n,m,t=[int(x) for x in stdin.readline().rstrip().split()]
A=[int(x) for x in stdin.readline().rstrip().split()]
graph1=[[] for _ in range(n)]
graph2=[[] for _ in range(n)]
for i in range(m):
    ta,tb,tc=[int(x) for x in stdin.readline().rstrip().split()]
    a=ta-1
    b=tb-1
    graph1[a].append((b,tc))
    graph2[b].append((a,tc))

def dijk(st,graph):
    inf=10**20
    dist=[inf]*n
    dist[st]=0
    hq=[[0,st]]
    # heapify(hq)
    seen=[False]*n
    while hq:
        v=heappop(hq)[1]
        seen[v]=True
        for to,cost in graph[v]:
            if seen[to]==False and dist[v]+cost<dist[to]:
                dist[to]=dist[v]+cost
                heappush(hq,[dist[to],to])
    return dist

pt1=dijk(0,graph1)
pt2=dijk(0,graph2)
maxp=0
for i in range(n):
    maxp=max(maxp,(t-pt1[i]-pt2[i])*A[i])
print(maxp)