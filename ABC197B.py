from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

h,w,x,y=map(int,input().split())
x-=1
y-=1
s=[list(input()) for _ in range(h)]
def nfind(pi,pj):
    nx,ny,cnt=x+pi,y+pj,0
    while 0<=nx and 0<=ny and nx<h and ny<w and s[nx][ny]=='.':
        cnt+=1
        nx+=pi
        ny+=pj
    return cnt
d=[(0,1),(0,-1),(1,0),(-1,0)]
print(sum(nfind(n,m) for n,m in d)+1)