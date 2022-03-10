n,m=map(int,input().split())
graph=[[] for _ in range(n)]
for i in range(m):
    a,b=map(lambda t:int(t)-1,input().split())
    graph[a]+=[b]
    graph[b]+=[a]
from sys import setrecursionlimit
setrecursionlimit(10**7)
reached=[False]*n;reached[0]=True;cnt=0
def dfs(i):
    global cnt
    if all(reached):cnt+=1
    for v in graph[i]:
        if not reached[v]:
            reached[v]=True
            dfs(v)
            reached[v]=False
dfs(0)
print(cnt)