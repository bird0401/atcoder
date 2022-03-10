d=int(input());n=list(input());ln=len(n);mod=10**9+7
dp=[[[0]*d for _ in range(2)] for j in range(ln+1)]
dp[0][0][0]=1
for i in range(1,ln+1):
    num=int(n[i-1])
    for j in range(d):
        for k in range(10):
            dp[i][1][(j+k)%d]+=dp[i-1][1][j]
            dp[i][1][(j+k)%d]%=mod
        for k in range(num):
            dp[i][1][(j+k)%d]+=dp[i-1][0][j]
            dp[i][1][(j+k)%d]%=mod
        dp[i][0][(j+num)%d]+=dp[i-1][0][j]
        dp[i][0][(j+num)%d]%=mod
print(dp[ln][0][0]+dp[ln][1][0]-1)