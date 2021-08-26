from sys import stdin
input=lambda:stdin.readline().rstrip()
inf=10**20

v,t,s,d=map(int,input().split())
if v*t<=d<=v*s:
    print("No")
else:
    print("Yes")