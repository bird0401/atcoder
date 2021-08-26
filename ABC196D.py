from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

h,w,x,y=map(int,input().split())
ans=0
def dfs(i,bit,a,b):
    if i==h*w:
        global ans
        ans+=1
        return
    if bit>>i&1:
        dfs(i+1,bit,a,b)
        return
    if b:
        dfs(i+1,bit|1<<i,a,b-1)
    if a:
        if i%w!=w-1 and not bit<<(i+1)&1:
            dfs(i+2,bit|1<<i|1<<(i+1),a-1,b)
        if i+w<h*w:
            dfs(i+1,bit|1<<i|1<<(i+w),a-1,b)
dfs(0,0,x,y)
print(ans)
