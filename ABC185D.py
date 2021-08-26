from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20
from math import ceil

n,m=map(int,input().split())
a=list(map(int, input().split()))
a+=[0,n+1]
a.sort()

leng=[a[i+1]-a[i]-1 for i in range(m+1) if a[i+1]-a[i]-1>0]
ans=0
if len(leng)!=0:
    minl=min(leng)
    ans=sum(ceil(float(l)/minl) for l in leng)
print(ans)