from math import gcd
a,b,c,d=map(int,input().split())
l=c*d//gcd(c,d)
f=lambda d:b//d-(a-1)//d
print((b-a+1)-f(c)-f(d)+f(l))