h,w=map(int,input().split())
hw=[list(map(int,input().split())) for _ in range(h)]
wh=[[] for _ in range(w)]
for j in range(w):
    for i in range(h):
        wh[j].append(hw[i][j])
sh,sw=[],[]
for hs in hw:
    sh+=[sum(hs)]
for ws in wh:
    sw+=[sum(ws)]
ans=[[-1]*w for _ in range(h)]
for i in range(h):
    for j in range(w):
        ans[i][j]=sh[i]+sw[j]-hw[i][j]
for a in ans:
    print(*a)