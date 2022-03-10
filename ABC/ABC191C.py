from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

h,w=map(int,input().split())
m=[input() for _ in range(h)]
cnt=0
for i in range(h-1):
    for j in range(w-1):
        scnt=(m[i][j]+m[i+1][j]+m[i][j+1]+m[i+1][j+1]).count('#')
        if scnt==1 or scnt==3:
            cnt+=1
print(cnt)