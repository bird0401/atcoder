from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

n=int(input())
s=set()
for a in range(2,n+1):
    if a**2>n: break
    for b in range(2,n+1):
        if a**b<=n: s.add(a**b)
        else: break
print(n-len(s))