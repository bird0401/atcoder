n,m,q=map(int,input().split())
a=[0]*n
b=[0]*m
inf=10**20
maxes=[[0]*n for _ in range(m)]
asum,bsum,s=[0]*n,[0]*m,0
for i in range(q):
    t,x,y=map(int,input().split())
    x-=1
    if t==1:
        # asum+=y-a[x]
        
        # s+=y*m-bsum
        sa=sorted(a)
        l,r=0,inf
        while r-l>1:
            mid=(r+l)//2
            if b[mid]<y:
                l=mid
            else:
                r=mid
        pre=r
        while r-l>1:
            mid=(r+l)//2
            if b[mid]<a[x]:
                l=mid
            else:
                r=mid
        a[x]=y
            
        res=y*r
        s+=res-asum[x]
        asum[x]+=res
    else:
        # bsum+=y-b[x]
        b[x]=y
        # s+=y*n-asum
        sb=sorted(b)
    # print(max(max(a),max(b)))

    l,r=0,inf
    while r-l>1:
        mid=(r+l)//2
        if toten(x,mid)<m:
            l=mid
        else:
            r=mid
    
    print(a)
    print(b)
    
    for j in range(n):
        for k in range(m):
            maxes[j][k]=[max(a[j],b[k])]
    print(s)
    # print(sum(sum(maxe) for maxe in maxes))

# 2 2 4
# 1 1 10
# 2 1 20
# 2 2 5
# 1 1 30


