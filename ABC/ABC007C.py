r,C=map(int,input().split())
((sy,sx),(gy,gx))=(map(lambda t:int(t)-1,input().split()) for i in range(2))
c=[list(input()) for _ in range(r)]
from collections import deque
def bfs():
    q=deque([(sy,sx)])
    m=[[-1]*C for _ in range(r)]
    m[sy][sx]=0
    while q:
        pi,pj=q.popleft()
        if 0<=pi<r and 0<=pj<C and c[pi][pj]=='.':
            for i,j in [(1,0),(-1,0),(0,1),(0,-1)]:
                ni,nj=pi+i,pj+j
                if m[ni][nj]<0:
                    m[ni][nj]=m[pi][pj]+1
                    q.append((ni,nj))
    return m[gy][gx]
print(bfs())