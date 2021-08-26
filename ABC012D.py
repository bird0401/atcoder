from sys import stdin
input=lambda:stdin.readline().rstrip()

n,m=map(int,input().split())
graph=[[] for _ in range(n)]
for i in range(m):
    a,b,t=map(int,input().split())
    a-=1
    b-=1
    graph[a].append((b,t))
    graph[b].append((a,t))

from heapq import heappop,heappush
def dijk(st):
    seen=[False]*n
    dist=[10**20]*n
    dist[st]=0
    hq=[(dist[st],st)]
    while hq:
        v=heappop(hq)[1]
        if seen[v]==True:
            continue
        seen[v]=True
        for to,t in graph[v]:
            gcost=dist[v]+t
            if gcost<dist[to]:
                dist[to]=gcost
                heappush(hq,(gcost,to))
    # print(dist)
    return dist
ans=10**20
for i in range(n):
    ans=min(ans,max(dijk(i)))
print(ans)



