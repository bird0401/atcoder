from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20
from math import atan2,pi,cos,sin,sqrt

n=int(input())
x0,y0=map(int,input().split())
x,y=map(int,input().split())
p,q=(x0+x)/2.0,(y0+y)/2.0
theta,r=atan2(y0-q,x0-p)+2*pi/n,sqrt((x-x0)**2+(y-y0)**2)/2
print("{} {}".format(p+r*cos(theta),q+r*sin(theta)))
