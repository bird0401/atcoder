n,m=map(int,input().split())
c=list(map(int, input().split()))
inf=10**20
dp=[inf]*(n+1)
dp[0]=0
for mo in c:
    for pri in range(mo,n+1):
        dp[pri]=min(dp[pri],dp[pri-mo]+1)
print(dp[n])