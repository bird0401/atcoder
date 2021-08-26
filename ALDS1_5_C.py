n=int(input())
from math import cos,sin,radians

def dot(a,b,c,m,r):
    if c==1:
        ans=[0]*r
        for j in range(r):
            for k in range(m):
                ans[j]+=a[k]*b[k][j]
    elif r==1:
        ans=[0]*c
        for j in range(c):
            for k in range(m):
                ans[j]+=a[j][k]*b[k]
    else:
        ans=[[0]*r for i in range(c)]
        for i in range(c):
            for j in range(r):
                for k in range(m):
                    ans[i][j]+=a[i][k]*b[k][j]
    return ans

def koch(d,p1,p2):
    if d==0:return 
    cos60,sin60=cos(radians(60)),sin(radians(60))
    af=[[cos60,-sin60],[sin60,cos60]]
    s=[float(2*e1+e2)/3 for e1,e2 in zip(p1,p2)]
    t=[float(e1+2*e2)/3 for e1,e2 in zip(p1,p2)]
    diff=[e2-e1 for e1,e2 in zip(s,t)]
    u=[e1+e2 for e1,e2 in zip(dot(af,diff,2,2,1),s)]
    koch(d-1,p1,s)
    print(*s)
    koch(d-1,s,u)
    print(*u)
    koch(d-1,u,t)
    print(*t)
    koch(d-1,t,p2)

p1,p2=[0,0],[100,0]
print(*p1)
koch(n,p1,p2)
print(*p2)