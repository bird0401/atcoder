d,n=map(int,input().split())
t=[int(input()) for _ in range(d)]
abc=[list(map(int, input().split())) for _ in range(n)]
dp=[[0]*n for _ in range(d)]
for i in range(1,d):
    for j in range(n):
        a,b,c=abc[j]
        for pj in range(n):
            pa,pb,pc=abc[pj]
            if a<=t[i]<=b and pa<=t[i-1]<=pb:
                dp[i][j]=max(dp[i][j],dp[i-1][pj]+abs(pc-c))
print(max(dp[d-1]))
