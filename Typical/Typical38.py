from math import *
mod=10**18
a,b=map(int,input().split())
ans=a*b//gcd(a,b)
print("Large" if ans>mod else ans)