mod=10**9+7  
inf=float('inf')
  
q=int(input())
for _ in range(q):
    x=list(input())
    y=list(input())
    nX,nY=len(x)+1,len(y)+1
    dp = [[0]*nY for _ in range(nX)] 
    for i in range(1,nX):
        for j in range(1,nY):
            if x[i-1] == y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    print(dp[-1][-1])