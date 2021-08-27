n=int(input())
s=list(input())
dp=[[[0 for i in range(10)] for _ in range(2**10)] for _ in range(n+1)]
mod=998244353
for i in range(1,n+1):
    x=ord(s[i-1])-ord('A')
    for j in range(2**10):
        for k in range(10):
            dp[i][j][k]+=dp[i-1][j][k]
            if x==k:
                dp[i][j][k]+=dp[i-1][j][k]
                dp[i][j][k]%=mod
    for j in range(2**10):
        if j&(1<<x):continue
        for k in range(10):
            dp[i][j|(1<<x)][x]+=dp[i-1][j][k]
            dp[i][j|(1<<x)][x]%=mod
    dp[i][1<<x][x]+=1
    dp[i][1<<x][x]%=mod
sum=0
for j in range(2**10):
    for k in range(10):
        sum+=dp[n][j][k]
        sum%=mod
print(sum)