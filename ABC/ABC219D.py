n=int(input())
x,y=map(int,input().split())
ab=[list(map(int, input().split())) for _ in range(n)]
inf=10**10
dp=[[[inf]*(y+1) for i in range(x+1)] for j in range(n+1)]
dp[0][0][0]=0

for i,(a,b) in enumerate(ab):
    for j in range(x+1):
        for k in range(y+1):
            dp[i+1][j][k]=min(dp[i][j][k],dp[i+1][j][k])
            dp[i+1][min(j+a,x)][min(k+b,y)]=min(dp[i+1][min(j+a,x)][min(k+b,y)],dp[i][j][k]+1)
            
print(dp[n][x][y] if dp[n][x][y]!=inf else -1)