from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

n,x=map(int,input().split())
x*=100
for i in range(n):
    v,p=map(int,input().split())
    x-=v*p
    if x<0:
        print(i+1)
        exit()
print(-1)