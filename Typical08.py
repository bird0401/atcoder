n=int(input())
s=list(input())
a="atcoder"
dp=[[0]*(n+1) for _ in range(8)]
for i in range(n+1):
    dp[0][i]=1
for i in range(7):
    for j in range(n):
        dp[i+1][j+1]=dp[i+1][j]+dp[i][j] if a[i]==s[j] else dp[i+1][j]
# print(dp)
print(dp[7][n]%(10**9+7))