from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

n,T=map(int,input().split())
ts=list(map(int, input().split()))
ans=0
for i in range(1,n): ans+=min(ts[i]-ts[i-1],T)
print(ans+T)