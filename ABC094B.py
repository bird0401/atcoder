from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

n,m,x=map(int,input().split())
a=list(map(int, input().split()))
cnt=0
for i in range(m):
    if a[i]>x: break
    cnt+=1
print(min(cnt,m-cnt))