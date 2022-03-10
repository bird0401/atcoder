from sys import stdin
input=lambda:stdin.readline().rstrip()

n,m,r=map(int,input().split())
R=[int(x)-1 for x in input().split()]
# print(R)
graph=[[] for _ in range(n)]
for i in range(m):
    a,b,c=map(int,input().split())
    a-=1
    b-=1
    graph[a].append([b,c])
    graph[b].append([a,c])
# print(graph)
from heapq import heappop,heappush
def dijk(st):
    seen=[False]*n
    dist=[10**20]*n
    dist[st]=0
    hq=[(dist[st],st)]
    while hq:
        # print(hq)
        v=heappop(hq)[1]
        if seen[v]==True:
            continue
        seen[v]=True
        for to,t in graph[v]:
            # print(to)
            gcost=dist[v]+t
            if gcost<dist[to]:
                dist[to]=gcost
                heappush(hq,(gcost,to))
    return dist

alldist=[]
for i in range(n):
    alldist.append(dijk(i))
# print(alldist)

from sys import setrecursionlimit
setrecursionlimit(10**7)
reached=[False]*r

ans=10**8
def dfs(cnt,i,allcost):
    global ans
    if cnt==r:
        ans=min(ans,allcost)
        return 
    for k in range(r):
        if reached[k]==False:
            reached[k]=True
            if i==-1:
                dfs(cnt+1,k,0)
            else:
                dfs(cnt+1,k,allcost+alldist[R[i]][R[k]])
            reached[k]=False
dfs(0,-1,0)
print(ans)