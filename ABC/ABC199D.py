n,m=map(int,input().split())
graph=[[] for _ in range(n)]
for i in range(m):
    a,b=map(lambda t:int(t)-1,input().split())
    graph[a].append(b)
    graph[b].append(a)

from collections import deque
m=[-1]*n
def bfs(st):
    q=deque([[st,-1]])
    m[st]=3
    while q:
        no,pre=q.popleft()
        # m[no]=max(3-len(graph[no]),0)
        for i in graph[no]:
            if i==pre:continue
            print(m)
            if m[i]==-1:
                m[i]=2
                q.append([i,no])
            elif i in graph[pre]:
                m[i]-=1
                # graph[i].remove(no)
                m[i]=max(m[no],0)

for i in range(n):
    if m[i]==-1:bfs(i)
s=1
for i in range(n):
    s*=m[i]
print(m)
print(s)