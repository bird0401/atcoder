n,m=map(int,input().split())
graph=[[] for _ in range(n)]
for i in range(m):
    a,b=map(lambda t:int(t)-1,input().split())
    graph[a].append(b)
    graph[b].append(a)
def judge(no,vi):
    if len(vi)==n:return 1
    res=0
    for ne in graph[no]:
        if ne not in vi:res+=judge(ne,vi+[ne])
    return res
print(judge(0,[0]))