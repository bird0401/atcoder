from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20
from math import sqrt

def mean1(a):
    s,cnt=0,0
    for i in range(len(a)):
        if a[i]!=-1:
            s+=a[i]
            cnt+=1
    return float(s)/cnt

def mean2(a,x):
    sa,sx,cnt=0,0,0
    for i in range(len(a)):
        if a[i]!=-1 and x[i]!=-1:
            sa+=a[i]
            sx+=x[i]
            cnt+=1
    return float(sa)/cnt,float(sx)/cnt

def cor(a,x,ra,rx):
    s,t1,t2=0,0,0
    for i in range(len(a)):
        if a[i]!=-1 and x[i]!=-1:
            s+=(a[i]-ra)*(x[i]-rx)
            t1+=(a[i]-ra)**2
            t2+=(x[i]-rx)**2
    return 0 if t1==0 and t2==0 else float(s)/(sqrt(t1)*sqrt(t2))

def pred(usritm,a,y):
    s,t=0,0
    for i in range(c):
        if usritm[i][y]!=-1 and i!=a:
            ra,rx=mean2(usritm[a],usritm[i])
            co=cor(usritm[a],usritm[i],ra,rx)
            s+=co*(usritm[i][y]-rx)
            t+=abs(co)
    return mean1(usritm[a])+s/t

c,r,a,y=map(int,input().split())
usritm=[list(map(int, input().split())) for _ in range(c)]
print(pred(usritm,a,y))
