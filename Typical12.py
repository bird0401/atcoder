from collections import defaultdict
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
    def find(self, x):
        if self.parents[x] < 0:return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:return
        if self.parents[x] > self.parents[y]:x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
    def size(self, x):
        return -self.parents[self.find(x)]
    def same(self, x, y):
        return self.find(x) == self.find(y)
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]
    def group_count(self):
        return len(self.roots())
    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members
    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

h,w=map(int,input().split())
un=UnionFind(h*w)
used=[[False]*w for _ in range(h)]
Q=int(input())

def f1(pi,pj):
    for di,dj in [[1,0],[-1,0],[0,1],[0,-1]]:
        ni,nj=pi+di,pj+dj
        if 0<=ni<h and 0<=nj<w and used[ni][nj]:un.union(w*pi+pj,w*ni+nj)

def f2(si,sj,gi,gj):
    if used[si][sj] and used[gi][gj] and un.same(w*si+sj,w*gi+gj):print("Yes")
    else:print("No")

for i in range(Q):
    q=list(map(lambda t:int(t)-1,input().split()))
    if q[0]:f2(q[1],q[2],q[3],q[4])
    else:used[q[1]][q[2]]=True;f1(q[1],q[2])
    