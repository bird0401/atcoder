from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20
from math import sqrt,floor
    
n=int(input())

def prime(n):
    cnt=0
    for i in range(1,int(floor(sqrt(n)))+1):
        if n%i==0:
            a=i
            b=n/i
            if (a+b)%2==1:
                cnt+=1
    return cnt*2

print(prime(2*n))
