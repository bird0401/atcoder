n=int(input())
graph=[[] for _ in range(n)]
for i in range(n-1):
    a,b=map(lambda t:int(t)-1,input().split())
    graph[a].append(b)
    graph[b].append(a)

from collections import deque
def bfs(s):
    q=deque([s])
    m=[-1]*n
    m[s]=0
    while q:
        no=q.popleft()
        for i in graph[no]:
            if m[i]<0:
                m[i]=m[no]+1
                q.append(i)
    mm,ma=0,-1
    for i in range(n):
        if mm<m[i]:mm,ma=m[i],i
    return mm,ma
mm,ma=bfs(0)
mm,ma=bfs(ma)
print(mm+1)