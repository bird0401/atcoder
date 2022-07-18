mod=10**9+7
inf=float('inf')
  
n,m=map(int,input().split())
t=[int(input()) for _ in range(n)]
c=[list(map(int, input().split())) for _ in range(m)]

dp=[[-inf]*m for _ in range(n+1)] #dp[i][j]: i日目にjの服を着る時の最大値
for i in range(1,n+1):
    for j in range(m):
        low,high,bri=c[j]
        if low<=t[i-1]<=high: 
            if i==1: dp[i][j]=0
            else: dp[i][j]=max(dp[i-1][k]+abs(bri-c[k][2]) for k in range(m))
# for e in dp: print(e)
print(max(dp[n]))