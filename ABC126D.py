from sys import stdin
from collections import deque

n=int(stdin.readline().rstrip())
graph=[[] for _ in range(n)]
for i in range(n-1):
    u,v,w=[int(x) for x in stdin.readline().rstrip().split()]
    u-=1
    v-=1
    graph[u].append([v,w])
    graph[v].append([u,w])
q=deque([0])
color=[-1]*n
color[0]=0
dist=[-1]*n
dist[0]=0
while q:
    p=q.popleft()
    # print(p)
    for adj,cost in graph[p]:
        if color[adj]==-1:
            dist[adj]=dist[p]+cost
            color[adj]=dist[adj]%2
            q.append(adj)
for i in range(n):
    print(color[i])
            
