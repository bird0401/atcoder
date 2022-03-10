from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

from math import factorial
def combination(n,r):
    return factorial(n)//(factorial(n-r)*factorial(r))
l=int(input())
print(combination(l-1,11))