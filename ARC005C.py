from sys import stdin
from collections import deque

h,w=[int(x) for x in stdin.readline().split()]
c=[list(input()) for _ in range(h)]
# print(c)

def bfs():
    for i in range(h):
        for j in range(w):
            if c[i][j]=='s':
                si=i
                sj=j
            if c[i][j]=='g':
                gi=i
                gj=j
            
    q=deque()
    q.append([si,sj])
    d=[[0,0,1,-1],[1,-1,0,0]]
    cost=[[10000]*w for _ in range(h)]
    cost[si][sj]=0
    while q:
        p=q.popleft()
        if p[0]==gi and p[1]==gj:
            # break
            continue
        for i in range(4):
            ni=p[0]+d[0][i]
            nj=p[1]+d[1][i]
            if 0<=ni<h and 0<=nj<w:
                ncost=cost[p[0]][p[1]]+(c[ni][nj]=='#')
                if ncost<=2 and ncost<cost[ni][nj]:
                    cost[ni][nj]=ncost
                    q.append([ni,nj])
    # print(cost)
    # print(cost[gi][gj])
    if cost[gi][gj]<=2:
        print("YES")
    else :
        print("NO")

bfs()
            