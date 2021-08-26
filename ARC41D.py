from sys import stdin
from collections import deque

n,m=[int(x) for x in stdin.readline().rstrip().split()]
graph=[[] for _ in range(n)]
for i in range(m):
    a,b,c=stdin.readline().rstrip().split()
    na=int(a)-1
    nb=int(b)-1
    graph[na].append([nb,int(c=='r')])
    graph[nb].append([na,int(c=='r')])

def bfs(sti,stc):
    q=deque([(sti,-1,stc)])
    color=[-1]*n
    cnt=0
    while q:
        p,pre,c=q.popleft()
        if color[p]==-1:
            color[p]=c
        else:
            if color[p]==c:
                continue
            else:
                return True
            
        for adj,nc in graph[p]:
            if adj!=pre and adj!=p and nc==c:
                q.append((adj,p,1-c))
                cnt+=1
    if cnt==m:
        return True
    else:
        return False

for i in range(n):
    for j in range(2):
        if bfs(i,j):
            print("Yes")
            exit()
print("No")