from sys import setrecursionlimit
setrecursionlimit(10**9)
def dfs(graph,pi,pj):
    for i,j in [(1,0),(-1,0),(0,1),(0,-1)]:
        ni,nj=pi+i,pj+j
        if 0<=ni<10 and 0<=nj<10 and graph[ni][nj]=='o':
            graph[ni][nj]='x';dfs(graph,ni,nj)

from copy import *
c=[list(input()) for _ in range(10)]
ans=[["x"]*10 for i in range(10)]
for i in range(10):
    for j in range(10):
        if c[i][j]=="x":
            c[i][j]="x";t=deepcopy(c);dfs(t,i,j)
            if t==ans:exit(print("YES"))
print("NO")
