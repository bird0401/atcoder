mod=10**9+7  
inf=float('inf')
  
n,m=map(int,input().split())  
c=list(map(int, input().split()))

dp=[[inf]*(n+1) for _ in range(m+1)]
for i in range(m+1):
    dp[i][0]=0

for i in range(1,m+1):
    for j in range(1,n+1):
        if j<c[i-1]: dp[i][j]=dp[i-1][j]
        else: dp[i][j]=min(dp[i-1][j],dp[i][j-c[i-1]]+1)

print(dp[m][n])