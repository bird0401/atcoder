from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

h,w=map(int,input().split())
s=[list(input()) for _ in range(h)]
dp=[[inf]*w for _ in range(h)] 
def dfs(pi,pj,flag,cnt):
    if not(0<=pi<h) or not(0<=pj<w): return
    if s[pi][pj]=='#' and flag==False:
        cnt+=1
        flag=True
    if s[pi][pj]=='.': flag=False
    if dp[pi][pj]<=cnt: return
    else: dp[pi][pj]=cnt
    dfs(pi+1,pj,flag,cnt)
    dfs(pi,pj+1,flag,cnt)
dfs(0,0,False,0)
print(dp[h-1][w-1])