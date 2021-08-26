n=int(input())
hw=[[0]*1001 for _ in range(1001)]
for _ in range(n):
    lx,ly,rx,ry=map(int,input().split())
    hw[lx][ly]+=1
    hw[rx][ry]+=1
    hw[lx][ry]-=1
    hw[rx][ly]-=1
for i in range(1001):
    for j in range(1,1001):
        hw[i][j]+=hw[i][j-1]
for j in range(1001):
    for i in range(1,1001):
        hw[i][j]+=hw[i-1][j]
ba=[0]*(n+1)
for i in range(1001):
    for j in range(1001):
        ba[hw[i][j]]+=1
for i in range(1,n+1):
    print(ba[i])