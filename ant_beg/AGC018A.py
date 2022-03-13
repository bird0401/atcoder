from math import gcd
n,k=map(int,input().split())  
a=list(map(int, input().split()))

ma=max(a)
p=a[0]
for e in a:
    p=gcd(p,e)
print("POSSIBLE" if k<=ma and k%p==0 else "IMPOSSIBLE")

