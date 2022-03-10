n,m,l,x=map(int,input().split())
A=list(map(int,input().split()))
inf=10**9;dp=[[inf]*m for i in range(n+1)]
dp[0][0]=1
for i in range(n):
    a=A[i]
    for j in range(m):
        dp[i+1][(j+a)%m]=min(dp[i][(j+a)%m],dp[i][j]+(j+a)//m)
print("Yes" if dp[-1][l]<=x else "No")
