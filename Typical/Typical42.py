k=int(input())
mod=10**9+7
dp=[0]*(k+1);dp[0]=1
for i in range(1,k+1):
    mi=min(9,i)
    for j in range(1,mi+1):
        dp[i]+=dp[i-j]
print(dp[k]%mod if k%9==0 else 0)
