from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

a,b=map(float,input().split())
print(100*(1-b/a))
