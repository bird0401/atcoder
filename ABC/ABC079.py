from sys import stdin
input=lambda:stdin.readline().rstrip()

h,w=map(int,input().split())
graph=[[int(x) for x in input().split()] for i in range(10)]
A=[[int(x) for x in input().split()] for i in range(h)]
# print(graph)

from heapq import heappop,heappush
def dijk(st):
    seen=[False]*10
    dist=[10**20]*10
    dist[st]=0
    hq=[(dist[st],st)]
    while hq:
        v=heappop(hq)[1]
        if seen[v]==True:
            continue
        seen[v]=True
        for to in range(10):
            cost=graph[v][to]
            gcost=dist[v]+cost
            if gcost<dist[to]:
                dist[to]=gcost
                heappush(hq,(gcost,to))
    return dist

alldist=[dijk(i) for i in range(10)]
# print(alldist)
sum=0
for i in range(h):
    for j in range(w):
        if A[i][j]==-1:
            continue
        else:
            sum+=alldist[A[i][j]][1]
print(sum)