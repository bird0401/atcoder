n=int(input())
graph=[[] for _ in range(n)]
col=[-1]*n
for i in range(n-1):
    a,b=map(lambda t:int(t)-1,input().split())
    graph[a]+=[b];graph[b]+=[a]
from sys import setrecursionlimit
setrecursionlimit(10**6)
def dfs(pos,cur):
    global col,graph
    col[pos]=cur
    for i in graph[pos]:
        if col[i]==-1:dfs(i,(cur+1)%2)
dfs(0,0)
a0,a1=[],[]
for i in range(n):
    if col[i]==0:a0+=[i+1]
    elif col[i]==1:a1+=[i+1]
if len(a0)>=n//2:print(*a0[:n//2])
else:print(*a1[:n//2])