# inf=float('inf')
inf=10**4

lim=10**6
dp=[inf]*lim # dp[i]: 正整数iを表すために必要な最小の正四面体数
dp[0]=0
dp_odd=[inf]*lim # 奇数のみ対象
dp_odd[0]=0

for n in range(1,10**2):
    w = n*(n+1)*(n+2)//6
    if w>=10**6: break
    for i in range(w,lim):
        v=dp[i-w]+1
        if dp[i]>v: dp[i]=v
    if w%2==1:
        for i in range(w,lim):
            v=dp_odd[i-w]+1
            if dp_odd[i]>v: dp_odd[i]=v

while True:
    k=int(input())
    if k==0: break
    print(f'{dp[k]} {dp_odd[k]}')