h,w=map(int,input().split())
c=[list(input()) for _ in range(h)]
cnt=0
for es in c:
    for e in es:
        if e=="#":cnt+=1

from collections import deque
def bfs(si,sj,gi,gj):
    q=deque([(si,sj)])
    m=[[-1]*w for _ in range(h)]
    m[si][sj]=0
    while q:
        pi,pj=q.popleft()
        for i,j in [(1,0),(-1,0),(0,1),(0,-1)]:
            ni,nj=pi+i,pj+j
            if 0<=ni<h and 0<=nj<w and c[pi][pj]=='.':
                if m[ni][nj]<0:
                    m[ni][nj]=m[pi][pj]+1
                    q.append((ni,nj))
    return m[gi][gj]

res=bfs(0,0,h-1,w-1)
print(-1 if res==-1 else h*w-cnt-(res+1))