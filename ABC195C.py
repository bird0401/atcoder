from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

n=int(input())
ans=0
if 10**3<=n: ans+=(n-10**3+1)*1
if 10**6<=n: ans+=(n-10**6+1)*2
if 10**9<=n: ans+=(n-10**9+1)*3
if 10**12<=n: ans+=(n-10**12+1)*4
if n==10**15: ans+=5
print(ans)