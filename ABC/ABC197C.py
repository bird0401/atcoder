from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

n=int(input())
x=list(map(int, input().split()))
ans=inf
for i in range(2**(n-1)):
    exs,ors=0,0
    for j in range(n):
        ors|=x[j]
        if (i>>j)&1:
            exs^=ors
            ors=0
    ans=min(ans,exs^ors)
print(ans)