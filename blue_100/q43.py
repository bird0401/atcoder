from collections import Counter

mod=10**9+7
inf=float('inf')

dic={'#':0,'B':1,'W':2,'R':3}
n=int(input())
s=[list(map(lambda t:dic[t], list(input()))) for _ in range(5)]
s=list(zip(*s))
cost=[[0]*4 for _ in range(n+1)]

for i in range(1,n+1):
    counter=Counter(s[i-1])
    for color in range(1,4):
        cost[i][color]=5-counter[color]

dp=[[inf]*4 for _ in range(n+1)] # dp[i][j] i列目まで走査した時に、i列目がj色の時の最小値
for i in range(4): dp[0][i]=0

for i in range(1,n+1):
    for j in range(1,4):
        dp[i][j]=min(dp[i-1][k]+cost[i][j] for k in range(1,4) if j!=k)
# for e in dp: print(e)
print(min(dp[-1]))