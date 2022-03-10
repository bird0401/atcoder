n=int(input())
graph=[[] for _ in range(n)]
for i in range(n-1):
    a,b=map(lambda t:int(t)-1,input().split())
    graph[a]+=[b];graph[b]+=[a]
dp=[[0]*2 for i in range(n)]
mod=10**9+7
def culc(node,color,past):
    if dp[node][color]!=0:return dp[node][color]
    elif len(graph[node])==1 and (past in graph[node]):
        dp[node][color]=1
        return 1
    sum=1
    for ch in graph[node]:
        if ch==past:continue
        if color:sum*=culc(ch,0,node);sum%=mod
        else:sum*=(culc(ch,0,node)+culc(ch,1,node));sum%=mod
    dp[node][color]=sum
    return sum

print((culc(0,0,-1)+culc(0,1,-1))%mod)