W=int(input())
n,k=map(int,input().split())
dp=[[0]*(k+1) for i in range(W+1)]
for i in range(1,n+1):
    w,v=map(int, input().split())
    for wei in range(W,w-1,-1):
        for kei in range(k,0,-1):
            dp[wei][kei]=max(dp[wei][kei],dp[wei-w][kei-1]+v)
print(dp[W][k])