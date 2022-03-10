from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

m,h=map(int,input().split())
if h%m==0: print("Yes")
else: print("No")