from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20
from math import sqrt,floor

n=int(input())
while True:
    for i in range(2,floor(sqrt(n))+1):
        if n%i==0:
            n+=1
            break
    else: exit(print(n))