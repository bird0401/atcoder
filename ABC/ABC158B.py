from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

n,a,b=map(int,input().split())
print((n//(a+b))*a+min(n%(a+b),a))