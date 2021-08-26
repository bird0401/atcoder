from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

n=int(input())
minp=inf
for i in range(n):
    a,p,x=map(int,input().split())
    if x-a>0:
        minp=min(minp,p)
if minp==inf: print(-1) 
else: print(minp)