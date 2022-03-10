from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

n=int(input())
xy=[list(map(int, input().split())) for _ in range(n)]
cnt=0
for i in range(n):
    for j in range(i+1,n):
        if -1<=float(xy[i][1]-xy[j][1])/(xy[i][0]-xy[j][0])<=1: cnt+=1
print(cnt)