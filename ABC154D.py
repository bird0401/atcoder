from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

n,k=map(int,input().split())
p=list(map(int, input().split()))
p.insert(0,0)
ns,maxs=sum(p[:k]),0
for i in range(n-k+1):
    ns+=(p[i+k]-p[i])
    if maxs<ns:
        maxs=ns
        ans=(ns+k)/2.0
print(ans)