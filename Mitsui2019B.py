from sys import stdin
from math import floor
input=lambda:stdin.readline().rstrip()

n=int(input())
for i in range(n+1):
    if int(floor(i*1.08))==n:
        print(i)
        exit()
print(":(")
    
