n,W=map(int,input().split())
dp=[0]*(W+1)
for _ in range(n):
    v,w=map(int, input().split())
    for wei in range(W,w-1,-1):
        dp[wei]=max(dp[wei],dp[wei-w]+v)
print(dp[W])