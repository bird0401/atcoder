mod=10**9+7
inf=float('inf')
# inf=10**10

ans=[]
lim=256
while True:
    n,m=map(int,input().split())
    if n==0 and m==0: break
    c=[int(input()) for _ in range(m)]
    x=[int(input()) for _ in range(n)]

    dp=[[inf]*(lim+1) for _ in range(n+1)] # dp[i][j]: i番目に到達した時に現在の周波数がjの時の累計最小値
    dp[0][128]=0

    for i in range(1,n+1):
        for j in range(lim+1):
            for k in range(m):
                next=min(max(0,j+c[k]),lim)
                dp[i][next]=min(dp[i][j],dp[i-1][j]+(x[i-1]-next)**2)
    ans.append(min(dp[n]))
print(dp[1][255])
for e in ans: print(e)