from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

n=int(input())
a=list(map(int, input().split()))
b=list(map(int, input().split()))
s=0
for i in range(n):
    s+=a[i]*b[i]
if s==0: print("Yes")
else: print("No")