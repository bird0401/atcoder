from bisect import bisect_left
n,W=map(int,input().split())
vw,vma,wma=[],0,0
for _ in range(n):
    v,w=map(int, input().split())
    vma,wma=max(vma,v),max(wma,w)
    vw.append([v,w])

def ml(a,sa):
    res=[]
    for i in range(2**sa):
        sv,sw=0,0
        for j in range(sa):
            if (i>>j)&1:
                sv+=a[j][0]
                sw+=a[j][1]
        res.append([sv,sw])
    res.sort(key=lambda t:t[1])
    # print(res)
    for i in range(2**sa-1):
        if res[i][0]>res[i+1][0]:res[i+1]=res[i]
    return res

if n<=30:
    sa=n//2
    a,b,ans=vw[:sa],vw[sa:],0
    ra,rb=ml(a,sa),ml(b,n-sa)
    ws=[w for v,w in ra]
    for bv,bw in rb:
        le=W-bw
        if le<0:continue 
        bl=bisect_left(ws,le)
        if bl==2**sa or ws[bl]!=le:bl-=1
        ans=max(ra[bl][0]+bv,ans)

elif vma<=1000:
    inf=10**20
    s=vma*n
    dp=[inf]*(s+1)
    dp[0]=0
    for v,w in vw:
        for i in range(s,-1,-1):
            dp[i]=min(dp[i],dp[i-v]+w)
    for i in range(s,-1,-1):
        if dp[i]<=W:
            ans=i
            break

elif wma<=1000:
    W=min(W,wma*n)
    dp=[0]*(W+1)
    for v,w in vw:
        for i in range(W,w-1,-1):
            dp[i]=max(dp[i],dp[i-w]+v)
    ans=dp[W]

print(ans)