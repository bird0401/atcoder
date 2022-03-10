d,g=map(int,input().split());g//=100
dp=[[0]*1001 for i in range(11)]
for i in range(1,d+1):
    p,c=map(int, input().split());c//=100
    for j in range(1001):
        for k in range(p):
            if j-k>=0:dp[i][j]=max(dp[i][j],dp[i-1][j-k]+k*i)
        if j-p>=0:dp[i][j]=max(dp[i][j],dp[i-1][j-p]+p*i+c)
for i in range(1001):
    if dp[d][i]>=g:print(i);break