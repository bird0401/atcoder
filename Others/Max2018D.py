n,m,l,x=map(int,input().split())
a=list(map(int, input().split()))
inf=10**5
dp=[[inf]*m for _ in range(n+1)]
dp[0][0]=1
for i in range(n):
    for j in range(m):
        t=j+a[i]
        dp[i+1][t%m]=min(dp[i][t%m],dp[i][j]+t//m)
print("Yes" if dp[n][l]<=x else "No")