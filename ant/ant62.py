n=int(input())
graph=[[] for _ in range(n)]
for i in range(n-1):
    a,b,d=map(int,input().split());a-=1;b-=1
    graph[a]+=[(b,d)]
    graph[b]+=[(a,d)]
from heapq import heappop,heappush
inf=10**20
def dijk(s):
    seen,dist=[False]*n,[inf]*n
    dist[s]=0
    hq=[(dist[s],s)]
    while hq:
        v=heappop(hq)[1]
        if seen[v]:continue
        seen[v]=True
        for to,cost in graph[v]:
            gcost=dist[v]+cost
            if gcost<dist[to]:
                dist[to]=gcost
                heappush(hq,(gcost,to))
    return dist

q,k=map(int, input().split());k-=1
dists=dijk(k)[:]
for i in range(q):
    x,y=map(lambda t:int(t)-1, input().split())
    print(dists[x]+dists[y])

