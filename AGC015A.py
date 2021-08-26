from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

n,a,b=map(int,input().split())
if n>1 and a<=b: print(b*(n-2)-a*(n-2)+1)
elif n==1 and a==b: print(1)
else: print(0)