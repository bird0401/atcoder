n=int(input())
x=list(map(int, input().split()))
right=x[-1]
x=x[:n-1]
dp=[[0]*21 for _ in range(n-1)]; dp[0][x[0]]=1

for i in range(1,n-1):
    num=x[i]
    for j in range(21):
        if 0<=j-num<21: dp[i][j]+=dp[i-1][j-num]
        if 0<=j+num<21: dp[i][j]+=dp[i-1][j+num]
print(dp[-1][right])