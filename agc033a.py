from sys import stdin
from collections import deque

h,w=[int(x) for x in stdin.readline().rstrip().split()]
m=[list(stdin.readline().rstrip()) for _ in range(h)]

def bfs():
    d=[[0,0,1,-1],[1,-1,0,0]]
    q=deque()
    dist=[[10000]*w for _ in range(h)]
        
    for i in range(h):
        for j in range(w):
            if m[i][j]=='#':
                q.append([i,j])
                dist[i][j]=0
    while q:
        p=q.popleft()
        for k in range(4):
            ni=p[0]+d[0][k]
            nj=p[1]+d[1][k]
            if ni>=0 and ni<h and nj>=0 and nj<w and m[ni][nj]=='.':
                m[ni][nj]='#'
                q.append([ni,nj])
                dist[ni][nj]=dist[p[0]][p[1]]+1
    # for i in range(h):
    #     print(dist[i])
    # print()
    print(max(max(i) for i in dist))

bfs()
