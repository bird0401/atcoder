from copy import deepcopy
l=[list(input()) for _ in range(10)]
xx=[['x']*10 for _ in range(10)]

def dfs(c,pi,pj):
    if 0<=pi<10 and 0<=pj<10 and c[pi][pj]=='o':
        c[pi][pj]='x'
        for di,dj in [(0,1),(0,-1),(1,0),(-1,0)]:dfs(c,pi+di,pj+dj)

for i in range(10):
    for j in range(10):
        if l[i][j]=='x':
            c=deepcopy(l)
            c[i][j]='o'
            dfs(c,i,j)
            if c==xx:exit(print("YES"))
print("NO")