from sys import stdin
input=lambda:stdin.readline().rstrip()
from math import ceil

h,w=map(int,input().split())
if h==1 or w==1:
    print(1)
else:print(ceil(h*w/2))
