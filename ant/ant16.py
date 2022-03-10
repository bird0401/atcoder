h,w,n=map(int,input().split())
c=[list(input()) for i in range(h)]
for i in range(h):
    for j in range(w):
        if c[i][j]=="S":si,sj=i,j

from collections import deque
def bfs(si,sj,goal):
    q=deque()
    q.append((si,sj))
    m=[[-1]*w for _ in range(h)]
    m[si][sj]=0
    while q:
        pi,pj=q.popleft()
        if c[pi][pj]==goal:return pi,pj,m[pi][pj]
        for i,j in [(1,0),(-1,0),(0,1),(0,-1)]:
            ni,nj=pi+i,pj+j
            if 0<=ni<h and 0<=nj<w and c[pi][pj]!='X' and m[ni][nj]<0:                
                m[ni][nj]=m[pi][pj]+1
                q.append((ni,nj))
ans=0
for i in range(1,n+1):
    si,sj,d=bfs(si,sj,str(i))
    ans+=d
print(ans)
