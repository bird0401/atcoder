mod=10**9+7  
inf=float('inf')
  
N,W=map(int,input().split())
dp=[0]*(W+1)  
for _ in range(N): 
    v,w=map(int, input().split())
    for wei in range(w,W+1):
        dp[wei]=max(dp[wei],dp[wei-w]+v)
print(dp[W])