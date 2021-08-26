from math import ceil
n,k=map(float,input().split())
a=list(map(int, input().split()))
print(ceil((n-1)/(k-1)))