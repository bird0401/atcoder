from sys import stdin
input=lambda:stdin.readline().rstrip()

n,m=map(int,input().split())
graph=[]
for i in range(m):
    a,b,c=map(int,input().split())
    graph.append([a-1,b-1,c])
INF=float('inf')

def bellman_ford():
    dist=[-INF]*n
    dist[0]=0
    for i in range(n):
        for fr,to,cost in graph:
            if dist[fr]+cost>dist[to]:
                dist[to]=dist[fr]+cost
                if i==n-1:
                    dist[to]=INF
    return dist

print(bellman_ford()[-1])
