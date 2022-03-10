from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

n=int(input())
a=list(map(int, input().split()))
pa=(n-1)*sum([x**2 for x in a])
ma,pile=0,0
for i in range(1,n):
    pile+=a[i-1]
    ma+=pile*a[i]
print(int(pa-2*ma))
