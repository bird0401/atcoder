MOD = 10**4
N, K = map(int, input().split())
A = [0] * (N+1)

for k in range(K):
    a, b = map(int, input().split())
    A[a] = b

# dp[n][i][j]: iを一日前に食べjを二日前に食べているような、n日目までのパターン数
# 1,2日目前が存在しない場合に備え、パスタ0を入れておく。パスタ指定とパスタが連続にならないかのみを考えれば良いためこれで成り立つ
dp = [[[0]*4 for i in range(4)] for j in range(N+1)] 
dp[0][0][0] = 1

for n in range(1,N+1):
    for i in range(4):
        for j in range(4):
            for k in range(1,4):
                if (A[n]==0 or A[n]==k) and (k != i or i != j): # パスタが指定されていないか指定のkと同じ場合で、三日連続ではない場合
                    dp[n][k][i] += dp[n-1][i][j]
                    dp[n][k][i] %= MOD
# for e in dp:
#     print(e)

ans = 0
for i in range(4): # 最終日、全ての状態の分を足す
    for j in range(4):
        ans += dp[-1][i][j]
        ans %= MOD

print (ans)