h,n=map(int,input().split())
inf=10**9;dp=[inf]*(h+1);dp[0]=0
for _ in range(n):
    w,v=map(int, input().split())
    for wei in range(w,h+1):
        dp[wei]=max(dp[wei],dp[wei-w]+v)
print(dp[h])