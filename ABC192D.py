from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

def toten(x,n):
    s=0
    for i in range(len(x)):
        s+=int(x[-1-i])*(n**i)
    return s
x=list(input())
m=int(input())
maxd=int(sorted(x,reverse=True)[0])
if len(x)==1:
    if int(x[0])>m: print(0)
    else: print(1)
    exit()
l,r=0,inf
while r-l>1:
    mid=(r+l)//2
    if toten(x,mid)<m:
        l=mid
    else:
        r=mid
if toten(x,r)>m:
    r-=1
print(max(0,r-maxd))
