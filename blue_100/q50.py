from sys import setrecursionlimit
INF =  float('inf')

setrecursionlimit(10**7)
N, M = map(int, input().split())
cost = [[[INF, 0] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    s, t, d, time = map(int, input().split())
    cost[s-1][t-1] = [d, time]
    cost[t-1][s-1] = [d, time]

#dp[S][v]:= 集合Sを訪問済みで最後にvにいる場合の最短時間を第一引数に、その場合の数を第二引数にもつ
dp = [[[-1] * 2 for _ in range(N)] for _ in range(1<<N)]
dp[0][0]=[0, 1]

def dfs(S, v):
    if dp[S][v] != [-1, -1]:
        return dp[S][v]

    if S&(1<<v) == 0:
        dp[S][v] = [INF, 0]
        return dp[S][v]
    
    v_time = INF
    v_s = 0
    for prev in range(N):
        prev_time, prev_s = dfs(S^(1<<v), prev)
        if prev_time + cost[prev][v][0] > cost[prev][v][1]:continue
        if v_time > prev_time + cost[prev][v][0]:
            v_time = prev_time + cost[prev][v][0]
            v_s = prev_s
        elif v_time == prev_time + cost[prev][v][0]:
            v_s += prev_s
    
    dp[S][v] = [v_time, v_s]
    return dp[S][v]

ans1, ans2 = dfs((1<<N)-1, 0)
if ans1 == INF:
    print("IMPOSSIBLE")
else:
    print(ans1, ans2)
    
