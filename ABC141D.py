inf=10**20
from heapq import *

n,m=map(int,input().split())
a=list(map(lambda e: -int(e), input().split()))
heapify(a)
for i in range(m): heappush(a,-(-heappop(a)//2))
print(-sum(a))