from sys import stdin
from collections import deque
input=lambda :stdin.readline().rstrip()

k=int(input())
dist=[10**20]*k
dist[1]=1
seen=[False]*10000
q=deque([1])
while q:
    p=q.popleft()
    x=(p*10)%k
    y=(p+1)%k
    dx=dist[p]
    dy=dist[p]+1
    if dx<dist[x]:
        dist[x]=dx
        q.append(x)
    if dy<dist[y]:
        dist[y]=dy
        q.append(y)
print(dist[0])
