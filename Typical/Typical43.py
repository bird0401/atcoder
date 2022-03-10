inf=10**20
h,w=map(int,input().split())
si,sj=map(lambda t:int(t)-1,input().split())
gi,gj=map(lambda t:int(t)-1,input().split())
s=[list(input()) for _ in range(h)]
dist=[[inf]*w for _ in range(h)]
d=[[1,0],[0,1],[-1,0],[0,-1]]
from collections import deque
def bfs():
    q=deque()
    dist[si][sj]=0;q.append([si,sj,-1,0])
    while q:
        pi,pj,di,c=q.popleft()
        for k in range(4):
            ni,nj=pi+d[k][0],pj+d[k][1]
            if 0<=ni<h and 0<=nj<w and s[ni][nj]=='.': 
                cost=c+(not(di==k or di==-1))
                if dist[ni][nj]>=cost:
                    dist[ni][nj]=cost
                    if di==k or di==-1:q.appendleft([ni,nj,k,cost])
                    else:q.append([ni,nj,k,cost])
bfs()
print(dist[gi][gj])