n,m=map(int,input().split())
c=[[-1]*n for i in range(n)]
for i in range(m):
    x,y=map(lambda t:int(t)-1,input().split())
    c[x][y]=1;c[y][x]=1
for i in range(n):
    c[i][i]=1
ans=-1
for i in range(2**n):
    gro=[];flag=0
    for j in range(n):
        if (i>>j)&1:gro+=[j]
    for e1 in gro:
        for e2 in gro:
            if c[e1][e2]!=1:flag=1;break
        if flag==1:break
    else:ans=max(ans,len(gro))
print(ans)