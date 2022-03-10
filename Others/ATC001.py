from sys import stdin
input=lambda:stdin.readline().rstrip()

h,w=map(int,input().split())
c=[list(input()) for _ in range(h)]

from sys import setrecursionlimit
setrecursionlimit(10**7)
reached=[[False]*w for _ in range(h)]
def dfs(pi,pj):
    if not(0<=pi<h) or not(0<=pj<w) or c[pi][pj]=='#':
        return
    if c[pi][pj]=='g':
        print("Yes")
        exit()
    c[pi][pj]='#'
    d=[(0,1),(0,-1),(1,0),(-1,0)]
    for (di,dj) in d:
        dfs(pi+di,pj+dj)
for i in range(h):
    for j in range(w):
        if c[i][j]=='s':
            si,sj=i,j
dfs(si,sj)
print("No")