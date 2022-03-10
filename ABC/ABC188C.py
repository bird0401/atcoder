from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

n=int(input())
a=list(map(int, input().split()))
b=a[:2**(n-1)]
c=a[2**(n-1):2**n]
mb=max(b)
mc=max(c)
ans=b.index(mb)+1 if mb<mc else c.index(mc)+2**(n-1)+1
print(ans)