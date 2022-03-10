n,m,x=map(int,input().split())
h=[int(input()) for i in range(n)]
graph=[[] for _ in range(n)]
for i in range(m):
    a,b,d=map(int,input().split());a-=1;b-=1
    if h[a]>=d:graph[a]+=[(b,d)]
    if h[b]>=d:graph[b]+=[(a,d)]
from heapq import heappop,heappush
inf=10**16
def dijk(s,g):
    seen,dist=[False]*n,[inf]*n
    dist[s]=0
    hq=[(dist[s],s)]
    while hq:
        v=heappop(hq)[1]
        if seen[v]:continue
        seen[v]=True
        for to,c in graph[v]:
            H=max(0,x-dist[v])
            if H-c<0:cost=2*c-H
            elif 0<=H-c<=h[to]:cost=c
            else:cost=H-h[to]
            gcost=dist[v]+cost
            if gcost<dist[to]:
                dist[to]=gcost
                heappush(hq,(gcost,to))
    return dist[g]+(h[g]-max(0,x-dist[g]))
ans=dijk(0,n-1)
print(ans if ans<inf else -1)