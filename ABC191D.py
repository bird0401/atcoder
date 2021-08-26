from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20
from math import ceil,floor,sqrt
from decimal import Decimal

x,y,r=map(Decimal,input().split())
cnt=0
for i in range(int(ceil(x-r)),int(floor(x+r))+1):
    dy=(r*r-(x-i)*(x-i)).sqrt()
    cnt+=floor(y+dy)-ceil(y-dy)+1
print(int(cnt))