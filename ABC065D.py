from sys import stdin
input=lambda:stdin.readline().rstrip()

from collections import defaultdict
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
    def size(self, x):
        return -self.parents[self.find(x)]
    def same(self, x, y):
        return self.find(x) == self.find(y)

n=int(input())
nodes=[]
for i in range(n):
    x,y=map(int,input().split())
    nodes.append((x,y,i))
uf=UnionFind(n)
sortx=sorted(nodes)
sorty=sorted(nodes,key=lambda i:i[1])
edges=[]
for i in range(n-1):
    costx=abs(sortx[i][0]-sortx[i+1][0])
    costy=abs(sortx[i][1]-sortx[i+1][1])
    cost=min(costx,costy)
    edges.append((cost,sortx[i][2],sortx[i+1][2]))
for i in range(n-1):
    costx=abs(sorty[i][0]-sorty[i+1][0])
    costy=abs(sorty[i][1]-sorty[i+1][1])
    cost=min(costx,costy)
    edges.append((cost,sorty[i][2],sorty[i+1][2]))
edges.sort()
ans=0
for edge in edges:
    c,fr,to=edge
    if not uf.same(fr,to):
        ans+=c
        uf.union(fr,to)
print(ans)