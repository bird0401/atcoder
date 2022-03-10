n,m=map(int,input().split())
from math import *
print(n*m if n==1 or m==1 else ceil(n/2)*ceil(m/2))
