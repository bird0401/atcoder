from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

n=int(input())
ab=[list(map(int, input().split())) for _ in range(n)]
minans=inf
for i in range(n):
    for j in range(n):
        a,b=ab[i][0],ab[j][1]
        ans=a+b if i==j else max(a,b)
        minans=min(minans,ans)
print(minans)