N = int(input())
A = [int(input()) for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)] #dp[i][[j]: A[i]からA[j]のケーキが残っている時のJOIの最大値
for i in range(N):
    for l in range(N):
        ln = (l+1)%N
        r = (l+i)%N
        rn = (r-1)%N
        if (N+i)%2: dp[l][r] = max(dp[ln][r]+A[l], dp[l][rn]+A[r]) # 左端のケーキと右端のケーキで大きい方
        else: dp[l][r] = dp[ln][r] if A[l]>A[r] else dp[l][rn] #A[l]の方が大きい場合はそちらを取るので、JOIはln~rの中から中から取る事になる

ans = max(dp[i][(i+N-1)%N] for i in range(N)) # 一周の仕方で値が変わるので注意。この中で最大値をansとする
# for e in dp: print(e)
print(ans)
