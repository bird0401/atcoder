from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

n,x=map(int,input().split())
a=list(map(int, input().split()))
b=[c for c in a if c!=x]
for i in range(len(b)):
    print(b[i],end=' ')
print("")