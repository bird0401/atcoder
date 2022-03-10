h,n=map(int,input().split())
inf=10**9;dp=[inf]*(h+1);dp[0]=0
for _ in range(n):
    w,v=map(int, input().split())
    for wei in range(h+1):
        dp[min(wei+w,h)]=min(dp[min(wei+w,h)],dp[wei]+v)
print(dp[h])