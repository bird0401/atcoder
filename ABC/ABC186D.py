from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

n=int(input())
a=list(map(int, input().split()))
a.sort(reverse=True)
suma,ans=sum(a),0
for i in range(n):
    suma-=a[i]
    ans+=a[i]*(n-i-1)-suma
print(ans)
