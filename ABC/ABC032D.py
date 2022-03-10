def culc(a,t):
    res1,res2=[[0,0]],[];global w
    for i in range(2**t):
        vs,ws=0,0
        for j in range(t):
            if (i>>j)&1:vs+=a[j][0];ws+=a[j][1]
        if ws<=w:res1+=[[vs,ws]]
    res1.sort(key=lambda t:t[1]);pre=-1
    for a,b in res1:
        if pre<a:res2+=[[a,b]];pre=a
    return res2
    
n,w=map(int,input().split())
vw=[list(map(int,input().split())) for i in range(n)]
ms=list(zip(*vw));mv,mw=max(ms[0]),max(ms[1])

if n<=30:
    t,ans=n//2,0
    vws1,vws2=culc(vw[:t],t),culc(vw[t:],n-t)
    ws=[W for V,W in vws2]
    from bisect import *
    for V,W in vws1:
        sub=w-W;bl=bisect(ws,sub)-1
        if bl>=0:ans=max(ans,V+vws2[bl][0])
    print(ans)
elif n<=200:
    if mw<=1000:
        w=min(w,mw*n);dp=[0]*(w+1)
        for V,W in vw:
            for i in range(w,W-1,-1):
                dp[i]=max(dp[i],dp[i-W]+V)
        print(dp[w])
    elif mv<=1000:
        v=mv*n;inf=10**20
        dp=[inf]*(v+1);dp[0]=0
        for V,W in vw:
            for i in range(v,V-1,-1):
                dp[i]=min(dp[i],dp[i-V]+W)
        for i in range(v,-1,-1):
            if dp[i]<=w:print(i);break