n,m=map(int,input().split())
graph=[[] for _ in range(n)]
for i in range(m):
    a,b=map(lambda t:int(t)-1,input().split())
    graph[a]+=[b]
    graph[b]+=[a]
reached,flag,cnt=[False]*n,True,0

def dfs(i,past):
    for v in graph[i]:
        global flag
        if v==past:continue
        if reached[v]:flag=False
        else:
            reached[v]=True
            dfs(v,i)

for i in range(n):
    flag=True
    if not reached[i]:
        dfs(i,-1)
        if flag:cnt+=1
print(cnt)
