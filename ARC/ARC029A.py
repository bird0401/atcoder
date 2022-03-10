n=int(input())
ts=[int(input()) for i in range(n)]
inf=10**20;ans=inf
for i in range(2**n):
    p1,p2=0,0
    for j in range(n):
        if (i>>j)&1:p2+=ts[j]
        else:p1+=ts[j]
    ans=min(ans,max(p1,p2))
print(ans)