mod=10**9+7
inf=float('inf')
  
n,m=map(int,input().split())
d=[int(input()) for _ in range(n)]
c=[int(input()) for _ in range(m)]

dp=[[inf]*(n+1) for _ in range(m+1)] # dp[i][j]:i日目に都市jにいるときのコストの最小値
for i in range(m+1):dp[i][0]=0

for i in range(1,m+1):
    for j in range(1,n+1):
        dp[i][j]=min(dp[i-1][j],dp[i-1][j-1]+c[i-1]*d[j-1])

# for e in dp:print(e)
print(dp[m][n])