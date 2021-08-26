from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

n=int(input())
a=list(map(int, input().split()))
b=[]
for i in range(n):
    b.append([a[i],i+1])
b.sort()
for i in range(n):
    print(b[i][1],end=" ")
print("")