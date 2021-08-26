from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

n=int(input())
v=list(map(int, input().split()))
v.sort()
sum=float(v[0])
for i in range(1,n):
    sum=(sum+v[i])/2
print(sum)