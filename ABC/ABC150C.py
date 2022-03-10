from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20
from itertools import permutations

n=int(input())
p=tuple(map(int, input().split()))
q=tuple(map(int, input().split()))
per=list(permutations(sorted(p),n))
def keysear(m):
    for i in range(len(per)):
        if per[i]==m: return i+1
a,b=keysear(p),keysear(q)
print(abs(a-b))