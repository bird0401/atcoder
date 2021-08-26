n,t=list(map(int, input().split()))
x=[int(input()) for _ in range(n)]
def f(p):
    k=0
    for i in range(t):
        s=0
        while s+x[k]<p:
            s+=x[k]
            k+=1
            if k==n:return k
    return k
inf=10**20
l,r=0,inf
while r-l>1:
    mid=(r+l)//2
    if f(mid)<n:
        l=mid
    else:
        r=mid
print(l) 