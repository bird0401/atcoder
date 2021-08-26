def lcs(s,t):
    n,m=len(s),len(t)
    dp=[0]*(m+1)
    for i in range(n):
        me=dp[:]
        for j in range(m):
            if s[i]==t[j]:dp[j+1]=me[j]+1
            elif dp[j+1]<dp[j]:dp[j+1]=dp[j]
    print(dp[m])

c=int(input())
for i in range(c):
    lcs(input(),input())