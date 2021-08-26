from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

n,k=map(int,input().split())
ans=0
for i in range(1,n+1):
    j=0
    while i*(2**j)<k: j+=1
    ans+=(1.0/n)/(2**j)
print(ans)