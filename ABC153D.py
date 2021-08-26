from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20
from math import log2,floor

h=int(input())
print(int(2**(floor(log2(h))+1)-1))